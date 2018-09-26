from flask import  render_template
from flask_script import Manager


from utils.functions import create_app

app = create_app()
manage = Manager(app=app)


if __name__ == '__main__':
    # app.run()
    manage.run()
