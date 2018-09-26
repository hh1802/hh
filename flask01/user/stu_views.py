from flask import Blueprint, render_template, request, make_response, redirect, url_for

stu_blueprint = Blueprint('stu',__name__)

@stu_blueprint.route('/hello/')
def hello():
    # 3/0
    return 'hello World!'


@stu_blueprint.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method =='GET':
        return render_template('login.html')
    if request.method =='POST':
        username = request.form.getlist('username')
        return render_template('login.html', username=username)


@stu_blueprint.route('/user_res/', methods=['GET', 'POST'])
def get_user_reponse():
    res = make_response('<h2>小萌妹</h2>',300)
    return res


@stu_blueprint.route('/redirect/', methods=['GET', 'POST'])
def user_redirect():
    # return redirect('stu/login/')
    return redirect(url_for('stu.login'))


@stu_blueprint.route('/hello/<name>/', methods=['GET', 'POST'])
def hello_world(name):
    return 'hello world %s' % name
