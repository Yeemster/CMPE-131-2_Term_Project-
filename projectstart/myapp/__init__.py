from flask import Flask
import os
from os import path
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



# create Flask class object named myobj
myobj = Flask(__name__)

myobj.config.from_mapping(
    SECRET_KEY = 'you-will-know',
    # location of sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    UPLOAD_FOLDER = 'md/markdown'
)

db = SQLAlchemy(myobj)

login = LoginManager(myobj)
# right side is the function that's called to login users
login.login_view ='auth.login'

from myapp import routes, models
from myapp.models import User, Note, ToDo, ToDo, FlashCard, notes

from .routes import views
from .auth import auth

myobj.register_blueprint(views, url_prefix='/')
myobj.register_blueprint(auth, url_prefix='/')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
DB_NAME = "database.db"
myobj = Flask(__name__)
db = SQLAlchemy(myobj)
def create_app():
    myobj.config['SECRET_KEY'] = 'you-will-know'
    myobj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    myobj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    myobj.config['UPLOAD_FOLDER'] = 'md/markdown'
    db.init_app(myobj)
    # migrate = Migrate(myobj, db)

    from .routes import views
    from .auth import auth

    myobj.register_blueprint(views, url_prefix='/')
    myobj.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, ToDo

    create_database(myobj)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(myobj)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return myobj


def create_database(app):
    if not path.exists('myapp/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
'''