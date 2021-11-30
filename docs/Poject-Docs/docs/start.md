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
Before starting 
## Project layout

```
CMPE-131-2_Term_Project-
└── projectstart  # dddd
    ├── myapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── auth.cpython-39.pyc
    │   │   ├── forms.cpython-38.pyc
    │   │   ├── forms.cpython-39.pyc
    │   │   ├── models.cpython-38.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── routes.cpython-38.pyc
    │   │   └── routes.cpython-39.pyc
    │   ├── app.db
    │   ├── auth.py
    │   ├── forms.py
    │   ├── md
    │   │   └── markdown
    │   │       ├── Specification.md
    │   │       ├── Specification.pdf
    │   │       └── transcript-2.png
    │   ├── models.py
    │   ├── routes.py
    │   └── templates
    │       ├── Main
    │       │   ├── main.html
    │       │   └── work.html
    │       ├── Timer
    │       │   └── pomodorotimer.html
    │       ├── authentication
    │       │   ├── account.html
    │       │   ├── log_out.html
    │       │   ├── login.html
    │       │   ├── sign_up.html
    │       │   └── update.html
    │       ├── base
    │       │   └── base/base/base.html
    │       ├── files
    │       │   └── mdopen.html
    │       ├── flashcards
    │       │   ├── add_flashcard.html
    │       │   ├── edit_flashcard.html
    │       │   ├── flashcards.html
    │       │   └── previewflashcards.html
    │       ├── notes
    │       │   ├── add_note.html
    │       │   ├── edit_note.html
    │       │   ├── notes.html
    │       │   ├── previewnotes.html
    │       │   ├── share_note.html
    │       │   └── unshare_note.html
    │       └── todos
    │           └── todolist.html
    └── run.py 
```