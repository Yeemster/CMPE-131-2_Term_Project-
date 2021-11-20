from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm, SignupForm
from flask import render_template, escape, flash, redirect, Blueprint 
from flask_login import  login_user, logout_user, login_required, current_user

views = Blueprint('views', __name__)


@views.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html", user=current_user)


@views.route("/work")
@login_required
def work():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("work.html", user=current_user)


'''
@myobj.route("/hi")
@login_required
def hi():
    return "Hi!"
'''
'''
@myobj.route("/members/<string:name>")
def getMember(name):
    return "hi: " + escape(name)
'''
'''
@myobj.route("/main")
def main():
    date = '2021-10-05'
    users = {'username':'carlos'}

    post = [ { 'author': 'John', 'body' : 'Beatutiful day in Portland!'},
            { 'author' : 'Susan', 'body' : 'The day is cloudy today!'}]

    return render_template('hello.html', users=users, datee=date, post=post)

'''

