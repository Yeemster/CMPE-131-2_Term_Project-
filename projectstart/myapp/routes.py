import re
from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, ToDo, Note, FlashCard, notes # todos
from myapp.forms import LoginForm, SignupForm, MDForm, NoteForm, ShareForm, FlashCardForm, UnshareForm, TimeForm
from flask import render_template, escape, flash, redirect, Blueprint, request, url_for
from flask_login import  login_user, logout_user, login_required, current_user
import markdown
import os
from werkzeug.utils import secure_filename
import streamlit as st
import time
from datetime import datetime

#from projectstart.myapp.forms import TimeForm

views = Blueprint('views', __name__)


@views.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("main.html", user=current_user)

@views.route("/work", methods=['GET', 'POST'])
@login_required
def work():
    """Return html template that passes in MDForm and the current user, allows links to user settings and import Markdown for rendering. 
    """
    form = MDForm()
    #if request.method == 'POST':
    if form.validate_on_submit():
        file = form.mdfile.data
        mdform = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                              myobj.config['UPLOAD_FOLDER'], 
                              secure_filename(file.filename))
        file.save(mdform)
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        with open(mdform, encoding="utf8") as mdfile:
            MDContent = markdown.markdown(mdfile.read())
            return render_template('mdopen.html', MDContent = MDContent, user=current_user)
        #return redirect(url_for("views.work"))
    return render_template("work.html", user=current_user, form=form)

@views.route("/todolist", methods=['GET','POST'])
@login_required
def todolist():
    user = User.query.filter_by(id=current_user.id).first()
    # todos = user.todos
    ordered_todos = ToDo.query.order_by(ToDo.rank)
    return render_template("todolist.html", user=current_user, todolist=ordered_todos)

@views.route("/todolist/add", methods=['POST'])
def add_todo():
    title = request.form.get("title")
    rank = request.form.get("rank")
    newtodo = ToDo(title=title, rank=rank, user_id=current_user.id, complete=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/change/<int:todos_id>")
def reload_todo(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/delete/<int:todos_id>")
def delete_todo(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    flash("Todo deleted", category="message")
    # current_user.todos.remove(todo)
    # user.notes.remove(todo_to_delete)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("views.todolist"))


# notes ---------------------------------------------------------------------------------------------

@views.route("/noteslist", methods=['GET','POST'])
@login_required
def noteslist():
    form = NoteForm() 
    user = User.query.filter_by(id=current_user.id).first() 
    notes = User.query.all() 
    usernotes = user.notes
    # check if the user owns the note to display the value for the user.
    note = form.note.data
    title = form.title.data
    return render_template("notes.html", form=form, user=current_user, noteslist=usernotes)

@views.route("/noteslist/preview/<int:id>", methods=['GET','POST'])
@login_required
def notes_preview(id):
    note = Note.query.filter_by(id=id).first()
    notedata = note.data
    MDContent = markdown.markdown(notedata)
    return render_template("previewnotes.html", MDContent=MDContent, user=current_user)

@views.route("/noteslist/add", methods=['POST','GET'])
def add_note():
    form = NoteForm() 
    mdform = MDForm()
    #data = request.form['Note']
    #if request.form == 'POST':
    if form.validate_on_submit():
        print('reached')
        data = form.note.data
        title = form.title.data
        newnote = Note(data=data, title=title, users=[current_user] )
        # assign an owner username who has sharing permissions
        username = newnote.users[0].username
        newnote.owner = username
        data = ''
        title = ''
        db.session.add(newnote)
        db.session.commit()
        flash("Successfully added new note")
        flash(f"Owner of note is { username }")
        return redirect(url_for("views.noteslist"))
    return render_template("add_note.html", form=form, user=current_user, mdform=mdform)
@views.route("/noteslist/add/import", methods=['GET','POST'])
def import_note():
    
    mdform = MDForm()
    form = NoteForm()
    #if request.method == 'POST':
    
    if mdform.validate_on_submit():
        print('reached1')
        file = mdform.mdfile.data
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        mdform1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(mdform1)
        with open(mdform1, 'r', encoding="utf8") as mdfile:
            form.note.data = mdfile.read()
        return redirect("/noteslist/add/import")    
    if form.validate_on_submit():
        print('reached')
        data = form.note.data
        title = form.title.data
        newnote = Note(data=data, title=title, user_id=current_user.id, )
        data = ''
        title = ''
        db.session.add(newnote)
        db.session.commit()
        flash("Successfully added new note")
        return redirect(url_for("views.noteslist"))
    return render_template("add_note.html", form=form, user=current_user, mdform=mdform)



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
    current_user.notes.remove(note)
    db.session.commit()
    return redirect(url_for("views.noteslist"))

@views.route("/noteslist/share/<int:id>", methods=['GET','POST'])
def share_note(id):
    note_to_share = Note.query.filter_by(id=id).first()
    form = ShareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_share_with = User.query.filter_by(username=user).first()
            user_to_share_with.notes.extend([note_to_share]) 
            note_to_share.shared = True
            db.session.commit()
            flash(f'Shared note with { user }', category="success")
            return redirect(url_for('views.noteslist'))
        else:
            flash(f'Failed to share note with { user }, invalid username', category="error")
    return render_template("share_note.html", form=form, user=current_user, note_to_share=note_to_share)   
@views.route("/noteslist/unshare/<int:id>", methods=['GET','POST'])
def unshare_note(id):
    note_to_unshare = Note.query.filter_by(id=id).first()
    form = UnshareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_unshare_with = User.query.filter_by(username=user).first()
            user_to_unshare_with.notes.remove(note_to_unshare)
            if len(note_to_unshare.users) <= 1: 
                note_to_unshare.shared = False
            db.session.commit()
            flash(f'Removed note from { user }', category="success")
            return redirect(url_for('views.noteslist'))
        else:
            flash(f'Failed to share note with { user }, invalid username', category="error")
    return render_template("unshare_note.html", form=form, user=current_user, note_to_unshare=note_to_unshare)   
def validate_username(username):
    username = User.query.filter_by(username=username).first()
    if username:
        return True
    else:
        return False 
    
# Flash Cards ----------------------------------------------------------------------------------------------
#     
@views.route("/flashcardslist", methods=['GET','POST'])
@login_required
def flashcardslist():
    form = FlashCardForm()
    #form = FlashCard() 
    user = User.query.filter_by(id=current_user.id).first()
    userflashcards = user.flashcards
    answer = form.answer.data
    question = form.question.data
    return render_template("flashcards.html", form=form, user=current_user, flashcardslist=userflashcards)

@views.route("/flashcardslist/preview/<int:id>", methods=['GET','POST'])
@login_required
def flashcards_preview(id):
    flashcards = FlashCard.query.filter_by(id=id).first()
    flashcardsanswer = flashcards.answer
    MDContent = markdown.markdown(flashcardsanswer)
    return render_template("previewflashcards.html", MDContent=MDContent, user=current_user)

@views.route("/flashcardslist/add", methods=['POST','GET'])
def add_flashcard():
    form = FlashCardForm() 
    mdform = MDForm()
    #data = request.form['Note']
    #if request.form == 'POST':
    if form.validate_on_submit():
        print('reached')
        answer = form.answer.data
        question = form.question.data
        newflashcard = FlashCard(answer=answer, question=question, author=current_user, user_id=current_user.id, )
        answer = ''
        question = ''
        db.session.add(newflashcard)
        db.session.commit()
        flash("Successfully added new flashcard")
        return redirect(url_for("views.flashcardslist"))
    return render_template("add_flashcard.html", form=form, user=current_user, mdform=mdform)

@views.route("/flashcardslist/update/<int:id>", methods=['GET','POST'])
def update_flashcard(id):
    flashcard_to_update = FlashCard.query.get_or_404(id)
    form = FlashCardForm()
    #data = request.form['Note']
    if form.validate_on_submit():
        print('reached')
        flashcard_to_update.answer = form.answer.data 
        flashcard_to_update.question = form.question.data
        # Update Database 
        db.session.add(flashcard_to_update)
        db.session.commit()
        flash("Note has been updated")
        return redirect(url_for("views.flashcardslist"))
    form.question.data = flashcard_to_update.question
    form.answer.data = flashcard_to_update.answer
    return render_template("edit_flashcard.html", form=form, user=current_user, flashcard_to_update=flashcard_to_update)

@views.route('/flashcardslist/delete/<int:id>', methods=['GET', 'POST' ])
@login_required
def delete_flashcards(id):
    #note = Note.query.get_or_404(id)
    flashcard = FlashCard.query.filter_by(id=id).first()
    db.session.delete(flashcard)
    db.session.commit()
    flash("Flashcard deleted", category="message")
    return redirect(url_for("views.flashcardslist"))

#@views.route('/ptimer/<int:t>', methods=['GET', 'POST' ])
#@login_required
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Fire in the hole!!')
    # return render_template("pomodorotimer.html", user = current_user, timer = timer)
    #return redirect(countdown(t))
    #t = input("Enter the time in seconds: ")
    #countdown(int(t))

@views.route('/ptimer', methods=['GET', 'POST' ])
@login_required
def timer():
    form = TimeForm()
    if form.validate_on_submit():
        print(form.countdown.data)
        #countdown(form.countdown.data)
        chars = form.countdown.data 
        charStr = datetime.now()
        tim = chars.strftime("%M:%S")
        print(type(tim))

        mins = int(tim[0:2])
        print(type(mins))
        print(mins)

        secs = int(tim[3:5])
        print(type(secs))
        print(secs)
        sum = (mins*60) + secs
        print(sum)
        countdown(sum)
        #minut = int(chars[3:4])
        #print(minut)
    return render_template("pomodorotimer.html", user = current_user, form = form)