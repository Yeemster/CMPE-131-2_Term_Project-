from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required

@myobj.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html")

@myobj.route("/hi")
@login_required
def hi():
    return "Hi!"

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
        login_user(user, remember=form.remember_me.data)
        return redirect('/')

    return render_template('login.html', form=form)

@myobj.route("/members/<string:name>")
def getMember(name):
    return "hi: " + escape(name)

@myobj.route("/main")
def main():
    date = '2021-10-05'
    users = {'username':'carlos'}

    post = [ { 'author': 'John', 'body' : 'Beatutiful day in Portland!'},\
            { 'author' : 'Susan', 'body' : 'The day is cloudy today!'}]

    return render_template('hello.html', users=users, datee=date, post=post)

@myobj.route("/logout")
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/')
