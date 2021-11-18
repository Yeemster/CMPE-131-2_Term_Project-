from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm, SignupForm
from flask import render_template, escape, flash, redirect, Blueprint 
from flask_login import  login_user, logout_user, login_required, current_user

#routes = Blueprint('views', __name__)
@myobj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        #login_user(user, remember=form.remember_me.data)
        else:
            flash('successfully signed in')
            return redirect('/work')
        return redirect('/')

    return render_template('login.html', form=form, user=current_user)

@myobj.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html", user=current_user)

@login_required
@myobj.route("/work")
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
@myobj.route("/sign-up", methods=['GET', 'POST'])
def signup():

    form = SignupForm()
    passwordform2 = SignupForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit() and passwordform2.validate_on_submit:
        flash(f'Registration requested for user {form.username.data}, {form.email.data} remember_me = {form.remember_me.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Email already exists.', category='error')
            return redirect('/sign-up')
        elif len(form.email.data) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            return redirect('/sign-up')
        elif len(form.username.data) < 2:
            flash('First name must be greater than 1 character.', category='error')
            return redirect('/sign-up')
        elif form.password.data != passwordform2.password.data:
            flash('Passwords don\'t match.', category='error')
            return redirect('/sign-up')
        elif len(form.password.data) < 7:
            flash('Password must be at least 7 characters.', category='error')
            return redirect('/sign-up')
        else:
            new_user = User(email=form.email.data, username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect("/work")
    return render_template('sign_up.html', form=form, form2=passwordform2, user=current_user)

@myobj.route("/logout")
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/')

