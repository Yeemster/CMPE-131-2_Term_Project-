from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm, SignupForm
from flask import render_template, escape, flash, redirect, Blueprint 
from flask_login import  login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category = 'error')
            return redirect(url_for("auth.login"))
        
        else:
            flash('successfully signed in', category = 'messsage')
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("views.work"))
        return redirect('/')

    return render_template('login.html', form=form, user=current_user)

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():

    form = SignupForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
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
        elif form.password.data != form.confirm_password.data:
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
            return redirect(url_for("views.work"))
    return render_template('sign_up.html', form=form, user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/')