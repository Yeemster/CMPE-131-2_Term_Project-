from flask_wtf import FlaskForm
from sqlalchemy.orm import query_expression
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired

from wtforms.validators import DataRequired, ValidationError, InputRequired, Length
from wtforms.widgets.core import TextArea

class LoginForm(FlaskForm):
    '''
    In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    username = StringField('User', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign in')

class SignupForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    email: WTF StringField requires String input, and Email validation.
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    username = StringField('User', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(max=60), validators.Email(message="Email is invalid")])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign up')

class UpdateUserForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    email: WTF StringField requires String input, and Email validation.
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
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

class ShareForm(FlaskForm):
    username = StringField("Enter Username to Share", widget=TextArea())
    submit = SubmitField('Share')
class FlashCardForm(FlaskForm):
    answer = StringField("answer", widget=TextArea())
    question = StringField("question", widget=TextArea())
    submit = SubmitField('Add')
