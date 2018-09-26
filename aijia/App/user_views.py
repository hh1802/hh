import os
import re

from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for
from App.models import db,User
from utils.setting import UPLOAD_DIR

aijiablueprient = Blueprint('user', __name__)

@aijiablueprient.route('/')
def hello():
    return 'hrl'



@aijiablueprient.route('/createdb/')
def createdb():
    db.create_all()
    return '创建数据库成功'


@aijiablueprient.route('/register/', methods=['GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')


@aijiablueprient.route('/register/', methods=['POST'])
def user_register():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([mobile, password,password2]):
            msg = '请填写完整的用户名或者密码'
            return jsonify({'code':1001, 'msg': msg})
        if not re.match(r'^1[345789]\d{9}$', mobile):
            msg = '用户名长度错误'
            return jsonify({'code':1002, 'msg':msg})
        user = User.query.filter_by(phone=mobile).all()
        if user:
            msg = '该用户已注册'
            return jsonify({'code':1003, 'msg':msg})
        else:
            if password != password2:
                msg = '两次密码不一致'
                return jsonify({'code':1004, 'msg':msg})
            else:
                u = User()
                u.phone = mobile
                u.password = password
                u.name = mobile
                u.add_update()
                # return render_template('login.html')
                return jsonify({'code':200, 'msg':'登录成功'})
#ajax提交
#

@aijiablueprient.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')




@aijiablueprient.route('/login/', methods=['POST'])
def user_login():
    mobile = request.form.get('mobile')
    password= request.form.get('password')
    if not all(['mobile', 'password']):
        return jsonify({'code':1005, 'msg':'登录的用户名或者密码为空'})
    if not re.match(r'^1[345789]\d{9}$', mobile):
        return jsonify({'code':1007, 'msg':'用户名长度不对'})
    user = User.query.filter_by(phone=mobile).first()
    if user:
        if not user.check_pwd(password):
            return jsonify({'code':1006, 'msg':'密码填写有误'})
        session['user_id'] = user.id
        return jsonify({'code':200, 'msg': '登录成功'})

    else:
        return jsonify({'code':1007, 'msg':'用户不存在'})


@aijiablueprient.route('/loginout/', methods=['GET'])
def loginout():
    session.clear()
    return redirect(url_for('user.login'))



@aijiablueprient.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')



@aijiablueprient.route('/user/', methods=['GET'])
def user_my():
    user = User.query.get(session['user_id'])
    data = user.to_basic_dict()
    return jsonify({'code':200, 'data':data})


@aijiablueprient.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')




@aijiablueprient.route('/profile/', methods=['PATCH'])
def avatar():
    file = request.files.get('avatar')
    if not re.match(r'^image.*$', file.mimetype):
        return jsonify({'code':1008, 'msg':'上传的格式不对'})
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(image_path)
    user = User.query.get(session['user_id'])
    avatar_path = os.path.join('upload', file.filename)
    user.avatar = avatar_path
    try:
        user.add_update()
    except Exception as e:
        db.session.rollback()
        return jsonify({'code':1009, 'msg':'数据库异常'})
    return jsonify({'code':200, 'msg':'上传图片成功', 'image_url':avatar_path})



# @aijiablueprient.route('/profile/', methods=['POST'])


#修改用户名信息，查询用户是否存在， ajax提交刷新到页面

@aijiablueprient.route('/proname/', methods=['PATCH'])
def proname():
    name = request.form.get('name')
    user = User.query.filter_by(name=name).first()
    if user:
        return jsonify({'code':1010, 'msg':'该用户已经存在'})
    else:
        u = User.query.get(session['user_id'])
        u.name = name
        u.add_update()
        return jsonify({'code':200, 'msg':'请求成功'})






@aijiablueprient.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


@aijiablueprient.route('/auth/',methods=['PATCH'])
def user_auth():
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')
    if not all([real_name, id_card]):
        return jsonify({'code':1011, 'msg':'用户名或者密码为空'})
    if not re.match(r'^[1-9]\d{17}$', id_card):
        return jsonify({'code':1012, 'msg':'身份证号不匹配'})
    user = User.query.get(session['user_id'])
    user.id_name = real_name
    user.id_card = id_card
    data = user.to_auth_dict()
    try:
        user.add_update()
    except:
        db.session.rollback()
    return jsonify({'code':200, 'msg':'请求成功'})


@aijiablueprient.route('/auths/', methods=['GET'])
def auths():
    user = User.query.get(session['user_id'])
    data = user.to_auth_dict()
    return jsonify({'code':200, 'msg':'请求成功', 'data':data})


# @aijiablueprient.route('/order/', methods=['GET'])
# def order():
#     return render_template('orders.html')
