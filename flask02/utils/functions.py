import os

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from App.hello_views import blueprinthello
from User.userviews import userblueprint
import redis


from utils.exts_init import ext_init

db = SQLAlchemy()

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)
    app.register_blueprint(blueprint=blueprinthello, url_prefix='/hello')
    app.register_blueprint(blueprint=userblueprint, url_prefix='/user')

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',port=6379)
    # se = Session()
    # se.init_app(app=app)
    app.config['SQLALCHEMY_TRACE_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/flask"
    app.debug = True
    app.config['SECRET_KEY'] = '<replace with a secret key>'

    ext_init(app)

    return app



