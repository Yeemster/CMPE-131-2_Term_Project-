# Getting Started

* `git clone [URL]` - Clone the code from Git hub https://github.com/razzacktiger/CMPE-131-2_Term_Project-
## Libraries from linux terminal:
* `pip install flask` - Install flask 
* `pip install flask-wtf` - Install WTforms for flask
* `pip install wtforms` - Install WTforms
* `pip install email-validator` - Install email validation for Wtforms
* `pip install flask-markdown` - Install flask markdown
*  or `pip install markdown`  - Or install Markdown
* `pip install flask-login` - Install flask
* `pip install flask-sqlalchemy ` - Install SQLalchemy for Flask
* `pip install -u werkzeug` - Install Werkzeug for security
* `pip install datetime` - Install Datetime


# Initialize Database File
1. Before starting, navigate to the projectstart file.
1. `python3` Run python3 IDE 
1. `from myapp import db` import db object
1. `from myapp.models import User, Notes, Note, FlashCard, ToDo` import tables from models including the association tabel 'Notes'
1. `quit()` exit out of IDE 
1. navigate to the projectstart file
1. `python3 run.py` Using this you should be able to run the application
## Project layout

```
CMPE-131-2_Term_Project-
C:.
|   .DS_Store
|   run.py
|
\---myapp
    |   .DS_Store
    |   app.db
    |   auth.py
    |   forms.py
    |   models.py
    |   routes.py
    |   __init__.py
    |
    +---css
    |       background.jpeg      
    |
    +---md
    |   \---markdown
    |           documentation.md 
    |           forms.md
    |           routes.md        
    |           Specification.md 
    |           Specification.pdf
    |
    +---static
    |   |   .DS_Store
    |   |
    |   +---css
    |   |       .DS_Store        
    |   |       style.css        
    |   |
    |   \---images
    |           .DS_Store        
    |           FlashCards.png   
    |           FlaskNotes.png   
    |           orange.png       
    |           orange2.jpeg     
    |           orange3.jpeg     
    |           ptimer.png       
    |           SIGNUP.png       
    |           Timer.png        
    |           ToDoList.png
    |           upload-file.png
    |           Upload.png
    |           YourAcc.png
    |
    +---templates
    |   |   .DS_Store
    |   |
    |   +---authentication
    |   |       account.html
    |   |       login.html
    |   |       log_out.html
    |   |       sign_up.html
    |   |       update.html
    |   |
    |   +---base
    |   |       base.html
    |   |
    |   +---files
    |   |       mdopen.html
    |   |       upload.html
    |   |
    |   +---flashcards
    |   |       add_flashcard.html
    |   |       edit_flashcard.html
    |   |       flashcards.html
    |   |       previewflashcards.html
    |   |       share_flashcard.html
    |   |       unshare_flashcard.html
    |   |
    |   +---Main
    |   |       .DS_Store
    |   |       main.html
    |   |
    |   +---notes
    |   |       add_note.html
    |   |       edit_note.html
    |   |       notes.html
    |   |       previewnotes.html
    |   |       share_note.html
    |   |       unshare_note.html
    |   |
    |   +---Timer
    |   |       ptimer.html
    |   |
    |   \---todos
    |           share_note.html
    |           share_todos.html
    |           todolist.html
    |
    \---__pycache__
            auth.cpython-39.pyc
            forms.cpython-38.pyc
            forms.cpython-39.pyc
            models.cpython-38.pyc
            models.cpython-39.pyc
            routes.cpython-38.pyc
            routes.cpython-39.pyc
            __init__.cpython-38.pyc
            __init__.cpython-39.pyc
```
