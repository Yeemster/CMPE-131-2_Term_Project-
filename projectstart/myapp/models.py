
from flask.helpers import flash
from myapp import db
# from myapp import login
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

notes = db.Table('notes',
                 db.Column('users_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('notes_id', db.Integer, db.ForeignKey('note.id')))
'''
todos = db.Table('todos',
                 db.Column('id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('id', db.Integer, db.ForeignKey('Todo.id')))
'''

class User(UserMixin, db.Model):
    '''
      User class holds the id, username, email, password, notes, todos, and flashcards of each user created.
      Has many to many relationships with class notes via association table.
    '''
    _tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash =db.Column(db.String(128))
    notes = db.relationship('Note', secondary=notes, backref=db.backref('author'))
    todos = db.relationship('ToDo', backref=db.backref('author'))
    # flash cards
    flashcards = db.relationship('FlashCard', backref='author', lazy='dynamic')

    def __repr__(self):
      '''
      returns username
      '''
        return f'<User  {self.username}>'

    def check_password(self, password):
      '''
      Returns the password entered. 
      '''
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
      '''
      Sets the password for each user
      returns none
      '''
        self.password_hash = generate_password_hash(password, method='sha256')


class Note(db.Model):
    '''
      Note class form holds the title, data, id, date, owner, and user_id for each note created by user from routes.py
      Parameter: None
      Return: None
    '''
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(100))
    data = db.Column(db.String(1000000))
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    shared = db.Column(db.Boolean, default=False)
    users = db.relationship('User', secondary=notes, backref=db.backref('note'))

class ToDo(db.Model):
  '''
  The ToDo Class is a class which holds the id, rank, title, completion, user_id, and users for each To Do that is added from routes.py
  Parameter: None
  Return: None
  '''
    __tablename__ = 'ToDo' 
    id = db.Column(db.Integer, primary_key= True)
    rank = db.Column(db.Integer)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', backref=db.backref('todo'))

class FlashCard(db.Model):
    '''
      FlashCard class form holds the question, answer, id, date, and user_id for each flash card created from routes.py
      Parameter: None
      Return: None
    '''
    id = db.Column(db.Integer, primary_key= True)
    answer = db.Column(db.String(1000))
    #data = db.Column(db.String(1000))
    question = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
