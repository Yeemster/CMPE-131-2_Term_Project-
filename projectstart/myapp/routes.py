from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post, ToDo, Note
from myapp.forms import LoginForm, SignupForm, MDForm, NoteForm
from flask import render_template, escape, flash, redirect, Blueprint, request, url_for
from flask_login import  login_user, logout_user, login_required, current_user
import markdown
import os
from werkzeug.utils import secure_filename
import time
#import streamlit as st

views = Blueprint('views', __name__)


@views.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html", user=current_user)


@views.route("/work", methods=['GET', 'POST'])
@login_required
def work():
    """Return H1 header that says welcome! (should be in html)
    """
    form = MDForm()

    if form.validate_on_submit():
        file = form.mdfile.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        mdform = os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        with open(mdform, encoding="utf8") as mdfile:
            MDContent = markdown.markdown(mdfile.read())
            return render_template('mdopen.html', MDContent = MDContent, user=current_user)
        #return redirect(url_for("views.work"))


    return render_template("work.html", user=current_user, form=form)

@views.route("/todolist", methods=['GET','POST'])
@login_required
def todolist():
    user = User.query.filter_by(id=current_user.id).first()
    userTodos = user.todos
    return render_template("todolist.html", user=current_user, todolist=userTodos)

@views.route("/todolist/add", methods=['POST'])
def add():
    title = request.form.get("title")
    newtodo = ToDo(title=title, user_id=current_user.id, complete=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/change/<int:todos_id>")
def reload(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/delete/<int:todos_id>")
def delete_todo(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("views.todolist"))

def pomodorotimer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        render_template()
        time.sleep(1)
        t -= 1

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




@views.route("/noteslist", methods=['GET','POST'])
@login_required
def noteslist():
    form = NoteForm() 
    user = User.query.filter_by(id=current_user.id).first()
    usernotes = user.notes
    note = form.note.data
    title = form.title.data
    return render_template("notes.html", form=form, user=current_user, noteslist=usernotes)

@views.route("/noteslist/preview/<int:id>", methods=['GET','POST'])
@login_required
def notes_preview(id):
    note = Note.query.filter_by(id=id).first()
    notedata = note.data
    print(notedata)
    print(type(notedata))
    MDContent = markdown.markdown(notedata)
    return render_template("previewnotes.html", MDContent=MDContent, user=current_user)

@views.route("/noteslist/add", methods=['POST','GET'])
def add_note():
    form = NoteForm() 

    #data = request.form['Note']
    #if request.form == 'POST':
    if form.validate_on_submit():
        print('reached')
        data = form.note.data
        title = form.title.data
        newnote = Note(data=data, title=title, author=current_user, user_id=current_user.id)
        data = ''
        title = ''
        db.session.add(newnote)
        db.session.commit()
        flash("Successfully added new note")
        return redirect(url_for("views.noteslist"))
    return render_template("add_note.html", form=form, user=current_user)

@views.route("/noteslist/update/<int:id>", methods=['GET','POST'])
def update_note(id):
    note_to_update = Note.query.get_or_404(id)
    form = NoteForm()
    #data = request.form['Note']
    if form.validate_on_submit():
        print('reached')
        note_to_update.data = form.note.data 
        note_to_update.title = form.title.data 
        # Update Database 
        db.session.add(note_to_update)
        db.session.commit()
        flash("Note has been updated")
        return redirect(url_for("views.noteslist"))
    form.title.data = note_to_update.title
    form.note.data = note_to_update.data
    return render_template("edit_note.html", form=form, user=current_user, note_to_update=note_to_update)

@views.route('/noteslist/delete/<int:id>', methods=['GET', 'POST' ])
@login_required
def delete_notes(id):
    #note = Note.query.get_or_404(id)
    note = Note.query.filter_by(id=id).first()
    flash("Note deleted", category="message")
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("views.noteslist"))
    



