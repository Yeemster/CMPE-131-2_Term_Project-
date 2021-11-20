from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms.validators import DataRequired, ValidationError, InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('User', validators=[InputRequired()])
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign in')

class SignupForm(FlaskForm):
    username = StringField('User', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(max=60), validators.Email(message="Email is invalid")])
    password = PasswordField('Password')
    confirm_password = PasswordField("Confirm Password")
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign up')

class UpdateUserForm(FlaskForm):
    username = StringField('User')
    email = StringField('Email', validators=[ Length(max=60), validators.Email(message="Email is invalid")])
    password = PasswordField('Password')
    confirm_password = PasswordField("Confirm Password")
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Update User')

class MDForm(FlaskForm):
    mdfile = FileField("File",validators=[FileRequired()])
    submit = SubmitField('Upload')