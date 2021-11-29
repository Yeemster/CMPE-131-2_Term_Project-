
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
        return f'<User  {self.username}>'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.timestamp}: {self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000000))
    title = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    shared = db.Column(db.Boolean, default=False)
    users = db.relationship('User', secondary=notes, backref=db.backref('note'))

class ToDo(db.Model):
    __tablename__ = 'ToDo' 
    id = db.Column(db.Integer, primary_key= True)
    rank = db.Column(db.Integer)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', backref=db.backref('todo'))

class FlashCard(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    answer = db.Column(db.String(1000))
    #data = db.Column(db.String(1000))
    question = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
