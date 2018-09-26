from flask import Blueprint, request, render_template, redirect, url_for, session
from User.models import db
from User.models import User,Grade,Student

stu_blueprint = Blueprint('stu', __name__)


@stu_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建数据库成功'


@stu_blueprint.route('/del_db/')
def del_db():
    db.drop_all()
    return '删除数据库成功'


@stu_blueprint.route('/hello_db/')
def hello_db():
    return 'hello'


@stu_blueprint.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if not all([username, password1, password2]):
            msg = '用户名或者密码为空'
            return render_template('register.html', msg=msg)

        else:
            if password1 != password2:
                msg = '两次密码不一致'
                return render_template('register.html', msg=msg)
            else:
                u = User(username, password1)
                u.save()
                return redirect(url_for('stu.login'))




@stu_blueprint.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            msg = '用户名或者密码出错'
            return render_template('login.html', msg=msg)
        else:
            user = User.query.filter_by(u_name=username, u_password=password).first()
            if not user:
                msg = '用户或者密码不对'
                return render_template('login.html', msg=msg)
            else:
                session['userid'] = user.u_id
            return redirect(url_for('stu.u_index'))


@stu_blueprint.route('/u_head/', methods=['GET','POST'])
def head():
    if request.method == 'GET':
        return render_template('head.html')




@stu_blueprint.route('/u_left/', methods=['GET','POST'])
def left():
    if request.method == 'GET':
        return render_template('left.html')


# @stu_blueprint.route('/u_grade/', methods=['GET','POST'])
# def u_grade():
#
#     return render_template('grade.html')




@stu_blueprint.route('/u_index/', methods=['GET','POST'])
def u_index():
    if request.method == 'GET':
        return render_template('index.html')



@stu_blueprint.route('/u_grade/', methods=['GET','POST'])
def show_addgrade():
    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        paginate = Grade.query.paginate(page, 3)
        grades = paginate.items

        return render_template('grade.html', grades=grades, paginate=paginate)


@stu_blueprint.route('/addgrade/', methods=['GET','POST'])
def addgrade():
    if request.method == 'GET':
        return render_template('addgrade.html')
    if request.method == 'POST':
        grade_name = request.form.get('grade_name')
        g = Grade(grade_name)
        db.session.add(g)
        db.session.commit()
        return redirect(url_for('stu.show_addgrade'))


@stu_blueprint.route('/editgrade/', methods=['GET','POST'])
def editgrade():
    if request.method == 'GET':
        grade_id = request.args.get('grade_id')
        return render_template('addgrade.html', grade_id=grade_id)
    if request.method == 'POST':
        gradeid = request.form['gardeid']
        g = Grade.query.get(gradeid)
        gardename = request.form['grade_name']
        g.g_name = gardename
        db.session.add(g)
        db.session.commit()
        return redirect(url_for('stu.show_addgrade'))



@stu_blueprint.route('/delgrade/', methods = ['GET', 'POST'])
def delgrade():
    if request.method == 'GET':
        grade_id = request.args.get('grade_id')
        g = Grade.query.get(grade_id)
        db.session.delete(g)
        db.session.commit()
        return redirect(url_for('stu.show_addgrade'))



@stu_blueprint.route('/class_list/', methods=['GET','POST'])
def class_list():
    if request.method == 'GET':
        return render_template('grade.html')




@stu_blueprint.route('/student/', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        students = Student.query.all()
        return render_template('student.html', students=students)


@stu_blueprint.route('/addstudent/', methods=['GET', 'POST'])
def addstudent():
    if request.method == 'GET':
        grades = Grade.query.all()
        return render_template('addstu.html', grades=grades)
    if request.method == 'POST':
        student_name = request.form.get('stuname')
        student_id = request.form.get('stuid')
        gradename = request.form.get('select_name')
        s = Student(student_id, student_name, gradename)
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('stu.student'))



@stu_blueprint.route('/delstu/')
def delstu():
    if request.method == 'GET':
        stuid = request.args.get('id')
        s = Student.query.get(stuid)
        db.session.delete(s)
        db.session.commit()

        return redirect(url_for('stu.student'))



@stu_blueprint.route('/editstu/', methods=['GET', 'POST'])
def editstu():
    if request.method == 'GET':
        stuid = request.args.get('id')
        s = Student.query.get(stuid)
        g = s.grade
        return render_template('addstu.html', g=g)
    if request.method == 'POST':
        gradeid = request.form.get('gradeid')
        gradename = request.form.get('select_name')
        g = Grade.query.get(gradeid)
        g.grades = gradename
        db.session.commit()
        return redirect(url_for('stu.student'))



@stu_blueprint.route('/role/', methods = ['GET','POST'])
def role():
    if request.method == 'GET':
        return render_template('roles.html')



@stu_blueprint.route('/addroles/', methods=['GET','POST'])
def addroles():
    if request.method == 'GET':
        return render_template('addroles.html')


@stu_blueprint.route('/permissions/')
def permissions():
    if request.method == 'GET':
        return render_template('permissions.html')


@stu_blueprint.route('/addpermission/')
def addpermission():
    if request.method == 'GET':
        return render_template('addpermission.html')