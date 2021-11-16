from flask import Flask
import os
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
)

db = SQLAlchemy(myobj)

login = LoginManager(myobj)
# right side is the function that's called to login users
login.login_view ='login'

from myapp import routes, models
