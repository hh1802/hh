from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_password1 = db.Column(db.String(16))
    create_time = db.Column(db.DateTime,default=datetime.now)

    __tablename__ = 'user'