from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=18)
    grades = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'student'
    def __init__(self, id, name, grades):
        self.s_id = id
        self.s_name = name
        self.grades = grades


class Grade(db.Model):
    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(16))
    g_create_time = db.Column(db.DateTime,default=datetime.now)
    students = db.relationship('Student', backref='grade', lazy=True)

    __tablename__ = 'grade'

    def __init__(self, name):
        self.g_name = name


class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_password = db.Column(db.String(16))
    u_create_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, password):
        self.u_name = name
        self.u_password = password


    def save(self):
        db.session.add(self)
        db.session.commit()



class Role(db.Model):
    r_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    r_name = db.Column(db.String(15))
    u_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=True)


class Permission(db.Model):
    p_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(10))