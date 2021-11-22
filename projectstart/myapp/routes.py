from flask.helpers import url_for
from myapp import myobj
from myapp import db
from myapp.models import User, Post, ToDo
from myapp.forms import LoginForm, SignupForm, MDForm
from flask import render_template, escape, flash, redirect, Blueprint, request, url_for
from flask_login import  login_user, logout_user, login_required, current_user
import markdown
import os
from werkzeug.utils import secure_filename
import streamlit as st

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

    

    #if request.method == 'POST':

    if form.validate_on_submit():
        file = form.mdfile.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        #mdform = os.path.join(myobj.root_path, 'md', secure_filename(file.filename))
        mdform = os.path.join(os.path.abspath(os.path.dirname(__file__)), myobj.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        with open(mdform) as mdfile:
            MDContent = markdown.markdown(mdfile.read())
            return render_template('mdopen.html', MDContent = MDContent, user=current_user)
        #return redirect(url_for("views.work"))
 

    return render_template("work.html", user=current_user, form=form)

@views.route("/todolist", methods=['GET','POST'])
@login_required
def todolist():
    todolist = ToDo.query.all()
    print(todolist)

    return render_template("todolist.html", user=current_user, todolist=todolist)

@views.route("/add", methods=['POST'])
def add():
    title = request.form.get("title")
    newtodo = ToDo(title=title, complete=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/change/<int:todos_id>")
def reload(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("views.todolist"))

@views.route("/delete/<int:todos_id>")
def delete(todos_id):
    todo = ToDo.query.filter_by(id=todos_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("views.todolist"))
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

