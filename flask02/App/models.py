from _datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=18)
    grades = db.Column(db.Integer,db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'student'

    def to_dict(self):
        return {
            's_id': self.s_id,
            's_name': self.s_name,
            's_age':self.s_age,
            'grade':self.grades,
        }


class Grade(db.Model):
    g_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    g_name = db.Column(db.String(16), unique=True, nullable=False)
    g_desc = db.Column(db.String(30), nullable=True)
    g_create_time = db.Column(db.DATE, default=datetime.now())
    students = db.relationship('Student', backref ='grade', lazy=True)
    __tablename__ = 'grade'


sc = db.Table('sc',
              db.Column('s_id', db.Integer, db.ForeignKey('student.s_id'), primary_key=True),
              db.Column('c_id', db.Integer, db.ForeignKey('courses.c_id'), primary_key=True))



class Course(db.Model):
    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(16), unique=True)
    students = db.relationship('Student', secondary=sc, backref='course')
    __tablename__ = 'courses'


    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name

    def to_dict(self):

        return {
            'c_id':self.c_id,
            'c_name':self.c_name,
            'students':[stu.to_dict() for stu in self.students],

        }

