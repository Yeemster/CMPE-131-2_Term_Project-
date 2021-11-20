from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post
from myapp.forms import LoginForm, SignupForm, UpdateUserForm
from flask import render_template, escape, flash, redirect, Blueprint, request 
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
            logout_user()
            flash(f'{current_user.username} logged out')
            login_user(user, remember=form.remember_me.data)
            flash('successfully signed in', category = 'messsage')
            return redirect(url_for("views.work"))
        return redirect('/')

    return render_template('login.html', form=form, user=current_user)

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        if request.method == 'POST':
            flash(f'Registration requested for user {form.username.data}, {form.email.data} remember_me = {form.remember_me.data}')
            user = User.query.filter_by(username=form.username.data).first()
            email = User.query.filter_by(email=form.email.data).first()
            if user:
                flash('User already exists.', category='error')
                return redirect(url_for("auth.signup"))
            if email:
                flash('User already exists.', category='error')
                return redirect(url_for("auth.signup"))
            elif len(form.email.data) < 4:
                flash('Email must be greater than 3 characters.', category='error')
                return redirect(url_for("auth.signup"))
            elif len(form.username.data) < 2:
                flash('First name must be greater than 1 character.', category='error')
                return redirect(url_for("auth.signup"))
            elif form.password.data != form.confirm_password.data:
                flash('Passwords don\'t match.', category='error')
                return redirect(url_for("auth.signup"))
            elif len(form.password.data) < 7:
                flash('Password must be at least 7 characters.', category='error')
                return redirect(url_for("auth.signup"))
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

@auth.route('/update/<int:id>', methods=['GET', 'POST' ])
@login_required
def update(id):
    form = UpdateUserForm()
    user_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('User already exists.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        if email:
            flash('User already exists.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif len(form.email.data) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif len(form.username.data) < 2:
            flash('First name must be greater than 1 character.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif ((form.password.data != '' or form.confirm_password.data != '') and (form.password.data != form.confirm_password.data)):
            flash('Passwords don\'t match.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif ((form.password.data != '' or form.confirm_password.data != '') and len(form.password.data) < 7):
            flash('Password must be at least 7 characters.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        else:
            password = ''
            username = ''
            email = ''
            password = form.password.data
            username = form.username.data
            email = form.email.data
            user_to_update.set_password(password)
            user_to_update.username = username
            user_to_update.email = email
            try:
                db.session.commit()
                flash("User updated successfully")
                return render_template("update.html", user=current_user, form=form, user_to_update=user_to_update)
            except:
                flash("Error updating user fields")
                return render_template("update.html", user=current_user, form=form, user_to_update=user_to_update)
    return render_template("update.html", user=current_user, form=form, user_to_update=user_to_update)

        
