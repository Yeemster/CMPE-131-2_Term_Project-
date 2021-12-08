from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User
from myapp.forms import LoginForm, SignupForm, UpdateUserForm
from flask import render_template, escape, flash, redirect, Blueprint, request 
from flask_login import  login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Generates the template for the login page, if user is validated, it redirects to the work page
            Parameters:
                    No paramters but contains a routing tag with "/login and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form and user.
    '''
    form = LoginForm()
    # if the user hit submit on the forms page
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category = 'error')
            return redirect(url_for("auth.login"))
        else:
            if current_user.is_authenticated:
                flash(f' logged out of {current_user.username}\'s account')
                logout_user()
            login_user(user, remember=form.remember_me.data)
            flash(f'successfully signed in to {current_user.username}', category = 'messsage')
            return redirect(url_for("views.home"))
    return render_template('authentication/login.html', form=form, user=current_user)


@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    '''
    Generates the template for the sign up page, if user submits valid data, it logs the user in and redirects to the work page
            Parameters:
                    No paramters but contains a routing tag with "/sign-up and methods of 'GET' and 'POST' passed through.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user).
    '''
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
                return redirect(url_for("views.home"))
    return render_template('authentication/sign_up.html', form=form, user=current_user)


@auth.route("/logout")
@login_required
def logout():
    '''
    Generates functionality for the logout template page, if user is signed in, it logs 
    the user out and redirects the user to the home page
            Parameters:
                    No paramters but contains a routing tag with "/logout" parameter
            Returns:
                    render_template(): Redirects the user to the home page
    ''' 
    logout_user()
    flash('User logged out')
    return redirect('/')

@auth.route('/update/<int:id>', methods=['GET', 'POST' ])
@login_required
def update(id):
    '''
    Generates functionality for the update user template page, if user is signed in, it prompts the user with updating form. 
    the fills out the neccessary changes to their account and the system redirects the user to the login page
            Parameters:
                    id (int): system passes in the given user's ID number associated in the User models table. 
                    Contains a routing tag with "/logout" parameter. Also Contains a @login_required tag to check authentication.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user) and user_to_update.
    '''
    form = UpdateUserForm()
    user_to_update = User.query.get_or_404(id)
    if request.method == 'POST':
        userq = User.query.filter_by(username=form.username.data).first()
        emailq = User.query.filter_by(email=form.email.data).first()
        password = form.password.data
        confirm_password = form.confirm_password.data
        username = form.username.data
        email = form.email.data
        if userq:
            flash('User already exists.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        if emailq:
            flash('User already exists.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif (email != '') and len(form.email.data) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif (username != '') and len(form.username.data) < 2:
            flash('First name must be greater than 1 character.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif ((password != '' or confirm_password != '') and (password != confirm_password)):
            flash('Passwords don\'t match.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        elif ((password != '' or confirm_password != '') and len(password) < 7):
            flash('Password must be at least 7 characters.', category='error')
            return redirect(url_for("auth.update", id=current_user.id))
        else:
            if password != '':
                user_to_update.set_password(password)
            if username != '':
                user_to_update.username = username
            if email != '':
                user_to_update.email = email
            try:
                db.session.commit()
                flash("User updated successfully")
                return render_template("update.html", user=current_user, form=form, user_to_update=user_to_update)
            except:
                flash("Error updating user fields")
                return render_template("update.html", user=current_user, form=form, user_to_update=user_to_update)
    return render_template("authentication/update.html", user=current_user, form=form, user_to_update=user_to_update)
@auth.route('/delete/<int:id>', methods=['GET', 'POST' ])
@login_required
def delete(id):
    '''
    Generates functionality for the delete user template page, if user is signed in, it deletes the account. Thus user is now logged out.
            Parameters:
                    id (int): system passes in the given user's ID number associated in the User models table. 
                    Contains a routing tag with "/logout" parameter. Also Contains a @login_required tag to check authentication.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user) and user_to_update.
    '''
    user_to_delete = User.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Successfully Deleted User")
    except:
        flash("Error occured in deleting user")
    return render_template("authentication/account.html", user=current_user)   


@auth.route("/account")
@login_required
def account():
    """
    Returns render_template() for html 
    account page consisting of user settings links
    """
    return render_template("authentication/account.html", user=current_user) 

    
