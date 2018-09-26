import random

from flask import Blueprint, render_template, request, redirect, url_for

from App.models import Student
from User.models import db,User


userblueprint = Blueprint('user', __name__)



@userblueprint.route('/logincreatedb/')
def logindb():
    db.create_all()
    return '创建成功logindb'


@userblueprint.route('/dellogindb/')
def dellogdb():
    db.drop_all()
    return '删除成功'



@userblueprint.route('/register/', methods=['GET','POST'])
def register():
    if request.method =='GET':
        return render_template('user_register.html')
    if request.method =='POST':
        username = request.form.get('username')
        pwd1 = request.form.get('password1')
        pwd2 = request.form.get('password2')
        if all([username, pwd1, pwd2]):
            if pwd1==pwd2:
                u = User()
                u.u_name = username
                u.u_password1 = pwd1
                u.u_password2 = pwd1
                db.session.add(u)
                db.session.commit()
            return render_template('user_login.html')


@userblueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('user_login.html')
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')


    # if request.method =='POST':
    #     u = User()
    #     u.u_name = '红哥'
    #     u.u_password = '123456'
    #     db.session.add(u)
    #     db.session.commit()


@userblueprint.route('/create_stus/', methods=['GET', 'POST'])
def create_stus():
    stu_list = []
    for i in range(10):
        stu = Student()
        stu.s_name = '温婉%s'%random.randrange(1000)
        stu.s_age = '%s'%random.randrange(18)
        stu_list.append(stu)
    db.session.add_all(stu_list)
    db.session.commit()

    return '创建小姐姐成功'


@userblueprint.route('/show_stus/', methods=['GET', 'POST'])
def showlist():
    if request.method=='GET':
        stu = Student.query.all()
        return render_template('students1.html', stu1=stu)



@userblueprint.route('/edit_stus/', methods=['GET', 'POST'])
def editstu():
    if request.method =='GET':
       id=request.args.get('id')
       stu1 = Student.query.filter_by(s_id=id).first()
       return render_template('editstu.html', stu =stu1)
    if request.method=='POST':
        id = request.form.get('id')
        username = request.form.get('username')
        age = request.form.get('age')
        stu = Student.query.filter_by(s_id=id).first()
        stu.s_name = username
        stu.s_age = age
        db.session.add(stu)
        db.session.commit()
        return redirect(url_for('user.showlist'))











@userblueprint.route('/paginate/', methods=['GET', 'POST'])
#分页
def paginate():
    if request.method=='GET':
        page = int(request.args.get('page', 1))
        paginate = Student.query.paginate(page, 2)
        stu = paginate.items
        return render_template('paginate.html', stu=stu, paginate=paginate)





@userblueprint.route('/register1/', methods=['GET', 'POST'])
def register1():
    pass
#注册


@userblueprint.route('/login1/', methods=['GET', 'POST'])
def login1():
    pass
#登录
#在数据库中查询与页面的是否一致








