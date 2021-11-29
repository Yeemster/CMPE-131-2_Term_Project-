from flask_wtf import FlaskForm
from sqlalchemy.orm import query_expression
from sqlalchemy.sql.functions import count
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms.validators import DataRequired, ValidationError, InputRequired, Length
from wtforms.widgets.core import TextArea

from projectstart.myapp.routes import countdown
from wtforms.fields.html5 import TimeField

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

class NoteForm(FlaskForm):
    note = StringField("Note", widget=TextArea())
    title = StringField("Title")
    submit = SubmitField('Post')

class FlashCardForm(FlaskForm):
    answer = StringField("answer", widget=TextArea())
    question = StringField("question", widget=TextArea())
    submit = SubmitField('Add')

class TimeForm(FlaskForm):
    submit = SubmitField('Start')
    countdown = TimeField('Countdown', format = '%M:%S')
