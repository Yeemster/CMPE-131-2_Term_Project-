from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm, SignupForm, MDForm
from flask import render_template, escape, flash, redirect, Blueprint 
from flask_login import  login_user, logout_user, login_required, current_user
import markdown
import os
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)


@views.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html", user=current_user)


@views.route("/work", methods=['GET', 'POST'])
@login_required
def work():
    """Return H1 header that says welcome! (should be in html)
    """
    form = MDForm()

    #if request.method == 'POST':

    if form.validate_on_submit():
        file = form.mdfile.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return redirect(url_for("views.work"))
 
    return render_template("work.html", user=current_user, form=form)


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

