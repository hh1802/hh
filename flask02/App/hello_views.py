from flask import Blueprint, render_template, make_response, request, session, redirect, url_for
from flask_restful import Resource

from App.models import db, Student, Grade, Course
from utils.exts_init import api

blueprinthello =Blueprint('hello', __name__)


@blueprinthello.route('/')
def hello():
    return 'hello'


@blueprinthello.route('/setcookie/')
def set_cookie():
    temp = render_template('cookies.html')
    res = make_response(temp)
    res.set_cookie('ticket', '123456', expires=10)
    return res

#s删除cookie
@blueprinthello.route('/delcookie/')
def del_cookie():
    temp = render_template('cookies.html')
    res = make_response(temp)
    res.delete_cookie()
    return res



@blueprinthello.route('/login/', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    if request.method =='POST':
        username = request.form.get('username')
        session['username'] = username
        return render_template('login.html', username=username)


@blueprinthello.route('/scores/', methods=['GET'])
def stu_scores():
    scores = [90, 80, 76, 56, 75, 12]
    return render_template('scores.html', scores=scores)



@blueprinthello.route('/createdb/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建成功'



@blueprinthello.route('/dropdb/', methods=['GET'])
def drop_db():
    db.drop_all()
    return '删除成功'


@blueprinthello.route('/create_stu/', methods=['GET'])
def create_stu():
    stu = Student()
    stu.s_name = '詹三'
    stu.s_age = '17'
    #创建数据
    db.session.add(stu)
    db.session.commit()
    return '创建学生成功'

@blueprinthello.route('/select_stu/', methods=['GET'])
def select_stu():
    #只要加all()变成list
    # stus = Student.query.filter(Student.s_name =='詹三')
    # stus = Student.query.filter_by(s_name ='詹三').all()
    # stus = Student.query.all()

    # return render_template('students.html', stus=stus)

    # stu = Student.query.filter_by(s_name ='詹三').first()
    # stu.s_name = '哈哈'
    # db.session.commit()

    stu = Student.query.filter_by(s_name='詹三').first()
    db.session.delete(stu)
    db.session.commit()
    return '删除成功'




@blueprinthello.route('/addgrade/', methods=['GET'])
def add_grade():
    if request.method =='GET':

        grades = {
            'python': '人生苦短',
            'php': '拍片',
            'java': '入门到放弃',
            'go': 'googg',
        }
        g_list = []
        for key in grades:
            g = Grade()
            g.g_name = key
            g.g_desc = grades[key]
            g_list.append(g)
        db.session.add_all(g_list)
        db.session.commit()

        return '创建班级成功'




@blueprinthello.route('/querygrade/', methods=['GET'])
def query_grade():
    grades = Grade.query.all()
    return render_template('grades.html', grades=grades)



@blueprinthello.route('/create_stu_by_grade/', methods=['GET', 'POST'])
def createstu():
    if request.method=='GET':
        g_id = request.args.get('g_id')
        return render_template('create_students.html', g_id=g_id)
    if request.method=='POST':
        gid = request.form.get('g_id')
        username = request.form.get('username')
        s = Student()
        s.s_name = username
        s.grades = gid
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('user.showlist'))








@blueprinthello.route('/selete_stu/', methods=['GET','POST'])
def selete_stu():
    if request.method=='GET':
        g_id = request.args.get('g_id')
        # g = Grade.query.get(g_id)
        g = Grade.query.filter_by(g_id=g_id).first()
        stu = g.students
        return render_template('students1.html',stu1=stu)


@blueprinthello.route('/create_course/', methods=['GET','POST'])
def create_c():
    if request.method =='GET':
        courses =['大学英语','大学数学','化学','生物','历史']
        c_list = []
        for key in courses:
            c = Course()
            c.c_name = key
            c_list.append(c)
        db.session.add_all(c_list)
        db.session.commit()

        return '创建课程成功'







@blueprinthello.route('/add_course/', methods=['GET','POST'])
def add_course():
    if request.method=='GET':
        courses = Course.query.all()
        return render_template('course.html', courses=courses)
    if request.method =='POST':
        #学生id可以直接从get请求里面直接获取
        id = request.args.get('id')
        #从页面里传过来通过select标签的name属性，获取option里面的值
        course_id = request.form.get('course')
        #不是操作第三张表，而是操作学生和课程表
        stu = Student.query.filter_by(s_id=id).first()
        course = Course.query.filter_by(c_id=course_id).first()
        course.students.append(stu)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('hello.query_grade'))
        #页面显示course




#通过学生查课程
@blueprinthello.route('/show_course/<int:id>/', methods=['GET','POST'])
def show_course(id):
    if request.method=='GET':
        stu = Student.query.get(id)
        courses = stu.course
        s_id = id
        return render_template('showcourse.html', courses=courses, s_id=s_id)


#删除课程
@blueprinthello.route('/stu/<int:s_id>/del_course/<int:c_id>/', methods=['GET','POST'])
def del_course(s_id, c_id):
    if request.method=='GET':
        stu = Student.query.get(s_id)
        course = Course.query.get(c_id)
        course.students.remove(stu)
        db.session.commit()
        return render_template('showcourse.html')



class CourseApi(Resource):
    def get(self):
        courses = Course.query.all()
        return {
            'code': 200,
            'msg':'请求成功',
            'data':[course.to_dict() for course in courses ],
        }


    def post(self):
        courses = ['小学语文', '小学数学', '小学化学', '小学生物', '小学历史']
        c_list = []
        for key in courses:
            c = Course()
            c.c_name = key
            c_list.append(c)
        db.session.add_all(c_list)
        db.session.commit()

        return '创建课程成功'
    def put(self):
        pass

    def patch(self):
        pass
    def delete(self, no):
        course = Course.query.get(no)
        db.session.delete(course)
        db.session.commit()
        return '删除课程成功'

#提炼到model里用面向对象,restful风格的返回格式
api.add_resource(CourseApi, '/api/course/','/api/course/<int:no>')