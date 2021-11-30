from flask_wtf import FlaskForm
from sqlalchemy.orm import query_expression
from sqlalchemy.sql.functions import count
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError, InputRequired, Length
from wtforms.widgets.core import TextArea
#from myapp.routes import countdown
# For linux/Ubuntu/Windows users use the improt below
from wtforms.fields import TimeField
# For mac users use the import below
# from wtforms.fields.html5 import TimeField
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
    '''
    *In forms.py
    Class: Defined as a Mark Down form using WTForms
            variables: 
                    mdfile: WTF FileField requires a File input
                    submit: Submitfield for submiting a file
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    mdfile = FileField("File",validators=[FileRequired()])
    submit = SubmitField('Upload')

class NoteForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a NoteForm form 
            variables: 
                    note: WTF StringField requires String input and text area
                    title:  WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    note = StringField("Note", widget=TextArea())
    title = StringField("Title")
    submit = SubmitField('Post')

class ShareForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a ShareForm form 
            variables: 
                    username: WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    username = StringField("Share to Username:", widget=TextArea())
    submit = SubmitField('Share')
class UnshareForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a UnshareForm form 
            variables: 
                    username: WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    username = StringField("Unshare Username", widget=TextArea())
    submit = SubmitField('Share')
class FlashCardForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a FlashCardForm form 
            variables: 
                    question: WTF StringField requires String input and text area
                    answer:  WTF StringField requires String input and text area
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    answer = StringField("answer", widget=TextArea())
    question = StringField("question", widget=TextArea())
    submit = SubmitField('Add')

class TimeForm(FlaskForm):
    '''
    *In forms.py
    Class: Defined as a TimeForm form 
            variables: 
                    countdown: TimeField for adding time in Minute : Second format
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
    submit = SubmitField('Start')
    countdown = TimeField('Countdown', format = '%M:%S')
