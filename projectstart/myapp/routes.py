import re
from flask.helpers import url_for
from myapp import myobj
from myapp import db
#from myapp import turbo
from myapp.models import User, ToDo, Note, FlashCard, Notes
from myapp.forms import LoginForm, SignupForm, MDForm, NoteForm, ShareForm, FlashCardForm, UnshareForm, TimeForm, pomorodoTimerForm
from flask import render_template, escape, flash, redirect, Blueprint, request, url_for
from flask_login import  login_user, logout_user, login_required, current_user
import markdown
import os
from werkzeug.utils import secure_filename
import time
from datetime import datetime
import pyttsx3 

#from projectstart.myapp.forms import TimeForm

views = Blueprint('views', __name__)


@views.route("/")
def home():
    """Return H1 header that says welcome! (should be in html)
    """
    return render_template("Main/main.html", user=current_user)

@views.route("/work", methods=['GET', 'POST'])
@login_required
def work():
    """Return html template that passes in MDForm and the current user, 
       allows links to user settings and import Markdown for rendering. 
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
            return render_template('files/mdopen.html', MDContent = MDContent, user=current_user)
        #return redirect(url_for("views.work"))
    return render_template("Main/work.html", user=current_user, form=form)

@views.route("/todolist", methods=['GET','POST'])
@login_required
def todolist():
    """
            Displays the option to input text for a todo list, and displays the list of todos from the database. 

            Parameters: 
                    No Parameters but contains a routing tag with “/todolist” and the methods of ‘GET’ and ‘POST’
            Returns:
                    render_template(): Renders the html template, which displays the ToDos in order.
    """
    # user = User.query.filter_by(id=current_user.id).first()
    # todos = user.todos
    ordered_todos = ToDo.query.order_by(ToDo.rank)
    # ordered_todos = user.todos
    return render_template("todos/todolist.html", user=current_user, todolist=ordered_todos)

@views.route("/todolist/add", methods=['POST'])
def add_todo():
    """
            Adds the new ToDo to the ToDo model and adds it to the database and commits. 

            Parameters:
                    No Parameters but contains a routing tag with “/todolist/add” and the method of ‘POST’
            Returns:
                    After being added it redirects to the todolist method, which then displays the new to do along with all the previous ones. 
    """
    title = request.form.get("title")
    rank = request.form.get("rank")
    newtodo = ToDo(title=title, rank=rank, users=[current_user], complete=False)
    username = newtodo.users[0].username
    newtodo.owner = username
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/change/<int:todos_id>")
def reload_todo(todos_id):
    """
            Reloads the status of completion for the selected To Do

            Parameter:
                    The selected todos id so that it knows which todo to reload. This method also contains a routing tag with "/todolist/change/<int:todos_id>".
            Returns:
                    After being reloaded it redirects to the todolist method, which then displays the updated to do along with all the previous ones. 
    """
    todo = ToDo.query.filter_by(id=todos_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/todolist/delete/<int:todos_id>")
def delete_todo(todos_id):
    """
            Deletes the selected  To Do from the database and displays a delete message

            Parameter: 
                    The selected todos id so that it knows which todo to delete. This method also contains a routing tag with "/todolist/delete/<int:todos_id>".
            Returns:
                    After being deleted it redirects to the todolist method, which then displays the list of todos without the deleted one
    """
    todo = ToDo.query.filter_by(id=todos_id).first()
    flash("Todo deleted", category="message")
    
    #current_user.todos.remove(todo)
    current_user.todos.remove(todo)
    db.session.commit()
    return redirect(url_for("views.todolist"))
@views.route("/todoslist/share/<int:id>", methods=['GET','POST'])
@login_required
def share_todo(id):
    '''
            Allows users to share notes with each other and edit them 
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/share/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_share.
    '''
    todo_to_share = ToDo.query.filter_by(id=id).first()
    form = ShareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_share_with = User.query.filter_by(username=user).first()
            user_to_share_with.todos.extend([todo_to_share]) 
            todo_to_share.shared = True
            db.session.commit()
            flash(f'Shared todo with { user }', category="success")
            return redirect(url_for('views.todoslist'))
        if not validate_username(user):
            print('here')
            flash(f'Failed to share todo with { user } invalid username')
    return render_template("todos/share_todo.html", form=form, user=current_user, todo_to_share=todo_to_share)   
@views.route("/todoslist/unshare/<int:id>", methods=['GET','POST'])
@login_required
def unshare_todo(id):
    '''
            Allows the user to unshare a note which was previously shared with other users
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/unshare/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_unshare.
    '''
    todo_to_unshare = ToDo.query.filter_by(id=id).first()
    form = UnshareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_unshare_with = User.query.filter_by(username=user).first()
            user_to_unshare_with.todos.remove(todo_to_unshare)
            if len(todo_to_unshare.users) <= 1: 
                todo_to_unshare.shared = False
            db.session.commit()
            flash(f'Removed todo from { user }', category="success")
            return redirect(url_for('views.todoslist'))
        else:
            flash(f'Failed to share todo with { user }, invalid username', category="error")
    return render_template("todos/unshare_todo.html", form=form, user=current_user, todo_to_unshare=todo_to_unshare)   

# notes ---------------------------------------------------------------------------------------------

@views.route("/noteslist", methods=['GET','POST'])
@login_required
def noteslist():
    '''
            Generates a notes list that is uniques to each user in the data base
            Parameters:
                    No paramters but contains a routing tag with "/noteslist and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and noteslist.
    '''
    form = NoteForm() 
    user = User.query.filter_by(id=current_user.id).first() 
    notes = User.query.all() 
    usernotes = user.notes
    # check if the user owns the note to display the value for the user.
    note = form.note.data
    title = form.title.data
    return render_template("notes/notes.html", form=form, user=current_user, noteslist=usernotes)

@views.route("/noteslist/preview/<int:id>", methods=['GET','POST'])
@login_required
def notes_preview(id):
    '''
            Function allows the user to preview notes added to the notes list
            Parameters:
                    Contains paramaters 'id' which is passed in by the routing tag "/noteslist/preview/<int:id>"
            Returns:
                    render_template(): Renders the html template given parameters MDContent and user.
    '''
    note = Note.query.filter_by(id=id).first()
    notedata = note.data
    MDContent = markdown.markdown(notedata)
    return render_template("notes/previewnotes.html", MDContent=MDContent, user=current_user)

@views.route("/noteslist/add", methods=['POST','GET'])
def add_note():
    '''
            Function allows user to add notes to the list and assign that user as an owner of the note
            Parameters:
                    No paramters but contains a routing tag with "/noteslist/add" and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and mdform.
    '''
    form = NoteForm() 
    mdform = MDForm()
    if mdform.validate_on_submit():
        print('reached1')
        file = mdform.mdfile.data
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        mdform1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(mdform1)
        with open(mdform1, encoding="utf8") as mdfile:
            content = mdfile.read()
            firstline = mdfile.readline()
        print(firstline)
        form.note.data = content
        form.title.data = firstline
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
    return render_template("notes/add_note.html", form=form, user=current_user, mdform=mdform)


@views.route("/noteslist/update/<int:id>", methods=['GET','POST'])
@login_required
def update_note(id):
    '''
            Function allows the user to edit notes previously created
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/update/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_update.
    '''
    note_to_update = Note.query.get_or_404(id)
    form = NoteForm()
    mdform = MDForm()
    #data = request.form['Note']
    if mdform.validate_on_submit():
        print('reached1')
        file = mdform.mdfile.data
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        mdform1 = os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(mdform1)
        with open(mdform1, encoding="utf8") as mdfile:
            content = mdfile.read()
        print(content)
        form.note.data = content

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
    return render_template("notes/edit_note.html", form=form, mdform=mdform, user=current_user, note_to_update=note_to_update)

@views.route('/noteslist/delete/<int:id>', methods=['GET', 'POST' ])
@login_required
def delete_notes(id):
    '''
            Function allows the user to delete a note previously created
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/delete/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    redirect (): redirects to notelist()
    '''
    #note = Note.query.get_or_404(id)
    note = Note.query.filter_by(id=id).first()
    flash("Note deleted", category="message")
    current_user.notes.remove(note)
    db.session.commit()
    return redirect(url_for("views.noteslist"))

@views.route("/noteslist/share/<int:id>", methods=['GET','POST'])
@login_required
def share_note(id):
    '''
            Allows users to share notes with each other and edit them 
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/share/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_share.
    '''
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
        if not validate_username(user):
            print('here')
            flash(f'Failed to share note with { user } invalid username')
    return render_template("notes/share_note.html", form=form, user=current_user, note_to_share=note_to_share)   
@views.route("/noteslist/unshare/<int:id>", methods=['GET','POST'])
@login_required
def unshare_note(id):
    '''
            Allows the user to unshare a note which was previously shared with other users
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/unshare/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_unshare.
    '''
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
    return render_template("notes/unshare_note.html", form=form, user=current_user, note_to_unshare=note_to_unshare)   
def validate_username(username):
    '''
            Function checks if username entered by the user is correct or not
            Parameters:
                    (str) username 
            Returns:
                    True or False
    '''
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
    '''
            Generates a flashcard list that is uniques to each user in the data base
            Parameters:
                    No paramters but contains a routing tag with "/flashcardslist" and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and flashcardslist.
    '''
    form = FlashCardForm()
    user = User.query.filter_by(id=current_user.id).first()
    userflashcards = user.flashcards
    answer = form.answer.data
    question = form.question.data
    return render_template("flashcards/flashcards.html", form=form, user=current_user, flashcardslist=userflashcards)


@views.route("/flashcardslist/preview/<int:id>", methods=['GET','POST'])
@login_required
def flashcards_preview(id):
    '''
     The function lets user preview a flashcasd previously created in markdown 
     Parameters:
                Contains parameter 'id' passed in through a routing tag
                "/flashcardslist/preview/<int:id>" with "methods of 'GET' and 'POST'
            
     Returns:
            render_template(): Renders the html template given parameters MDContent and user.
    '''
    flashcards = FlashCard.query.filter_by(id=id).first()
    flashcardsanswer = flashcards.answer
    MDContent = markdown.markdown(flashcardsanswer)
    return render_template("flashcards/previewflashcards.html", MDContent=MDContent, user=current_user)


@views.route("/flashcardslist/add", methods=['POST','GET'])
@login_required
def add_flashcard():
    '''
     The function lets user add a flashcard to their list  
     Parameters:
            No paramters but contains a routing tag "/flashcardslist/add" with "methods of 'GET' and 'POST'
     Returns:
            render_template(): Renders the html template given parameters form, mdform, and user.
    '''
    form = FlashCardForm() 
    if form.validate_on_submit():
        print('reached')
        answer = form.answer.data
        question = form.question.data
        newflashcard = FlashCard(answer=answer, question=question, users=[current_user] )
        answer = ''
        question = ''
        username = newflashcard.users[0].username
        newflashcard.owner = username
        db.session.add(newflashcard)
        db.session.commit()
        flash("Successfully added new flashcard")
        flash(f"Owner of flashcard is { username }")
        return redirect(url_for("views.flashcardslist"))
    return render_template("flashcards/add_flashcard.html", form=form, user=current_user)

@views.route("/flashcardslist/update/<int:id>", methods=['GET','POST'])
@login_required
def update_flashcard(id):
    '''
          Function allows the user to update the flash cards previously created
          Parameters:
                   Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/update/<int:id>" with "methods of 'GET' and 'POST'
          Returns:
                  render_template(): Renders the html template given parameters form, user, and flashcard_to_update.
    '''
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
    return render_template("flashcards/edit_flashcard.html", form=form, user=current_user, flashcard_to_update=flashcard_to_update)

@views.route('/flashcardslist/delete/<int:id>', methods=['GET', 'POST' ])
@login_required
def delete_flashcards(id):
    '''
            The function allows the user to delete flashcards in the list
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/delete/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    redirect(): redirects to flashcardslist()
    '''
    flashcard = FlashCard.query.filter_by(id=id).first()
    current_user.flashcards.remove(flashcard)
    db.session.commit()
    flash("Flashcard deleted", category="message")
    return redirect(url_for("views.flashcardslist"))

@views.route("/flashcardslist/share/<int:id>", methods=['GET','POST'])
@login_required
def share_flashcard(id):
    '''
            Allows users to share notes with each other and edit them 
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/share/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_share.
    '''
    flashcard_to_share = FlashCard.query.filter_by(id=id).first()
    form = ShareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_share_with = User.query.filter_by(username=user).first()
            user_to_share_with.flashcards.extend([flashcard_to_share]) 
            flashcard_to_share.shared = True
            db.session.commit()
            flash(f'Shared note with { user }', category="success")
            return redirect(url_for('views.flashcardslist'))
        else:
            flash(f'Failed to share flashcard with { user }, invalid username', category="error")
    return render_template("flashcards/share_flashcard.html", form=form, user=current_user, flashcard_to_share=flashcard_to_share)   
@views.route("/flashcardslist/unshare/<int:id>", methods=['GET','POST'])
@login_required
def unshare_flashcard(id):
    '''
            Allows the user to unshare a note which was previously shared with other users
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/unshare/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_unshare.
    '''
    flashcard_to_unshare = Note.query.filter_by(id=id).first()
    form = UnshareForm()
    if form.validate_on_submit():
        print('reached')
        user = form.username.data 
        if validate_username(user):
            user_to_unshare_with = User.query.filter_by(username=user).first()
            user_to_unshare_with.flashcards.remove(flashcard_to_unshare)
            if len(flashcard_to_unshare.users) <= 1: 
                flashcard_to_unshare.shared = False
            db.session.commit()
            flash(f'Removed note from { user }', category="success")
            return redirect(url_for('views.flashcardslist'))
        else:
            flash(f'Failed to share note with { user }, invalid username', category="error")
    return render_template("flashcards/unshare_flashcard.html", form=form, user=current_user, flashcard_to_unshare=flashcard_to_unshare)   






@views.route('/ptimer', methods=['GET', 'POST' ])
@login_required
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
def countdown():
    return render_template("Timer/ptimer.html", user = current_user)
    
    
    #return render_template("Timer/pomodorotimer.html", user = current_user, timer = timer)
    #return redirect(countdown(t))
    #t = input("Enter the time in seconds: ")
    #countdown(int(t))
