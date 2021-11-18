from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm
from flask import render_template, escape, flash, redirect, Blueprint 
from flask_login import current_user, login_user, logout_user, login_required

#auth = Blueprint('auth', __name__)

'''
@myobj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            redirect('/login')
        #login_user(user, remember=form.remember_me.data)
        return redirect('/')

    # return render_template('login.html', form=form)
'''

