from flask import Flask, session, redirect, url_for
from User.user_views import stu_blueprint
from User.models import db
import os
import redis



def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    app.register_blueprint(blueprint=stu_blueprint, url_prefix='/user')

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask2"
    db.init_app(app=app)

    return app


def is_login(func):
    def check_login():
        user_session = session.get('userid')
        if user_session:
            return func
        else:
            redirect(url_for('stu.login'))

    return check_login()


