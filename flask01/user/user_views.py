from flask import Blueprint, render_template



blue = Blueprint('first',__name__)


@blue.route('/hello/')
def hello():
    # 3/0
    return 'hello World!'

@blue.route('/helloman/<name>/')
def hello_man(name):
    return render_template('hello.html', name=name )

@blue.route('/helloint/<int:id>/')
def hello_int(id):
    return render_template('hello.html', id=id)

@blue.route('/hellepath/<path:path>/')
def hello_path(path):
    return render_template('hello.html', path=path)

@blue.route('/hellouuid/<uuid:uuid>/')
def hello_uuid(uuid):
    return render_template('hello.html', uuid=uuid)

