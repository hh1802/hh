from flask import Flask,session,redirect,url_for
from flask_session import Session
import os
import redis

from App.house_views import house_blueprint
from App.user_views import aijiablueprient
from App.models import db
se = Session()
def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    app.register_blueprint(blueprint=aijiablueprient, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flaskaj"
    db.init_app(app=app)
    se.init_app(app=app)
    return app


def is_login(fun):
    def check_login():
        if session['user_id']:
            return fun()
        else:
            return redirect(url_for('user.login'))

    return check_login