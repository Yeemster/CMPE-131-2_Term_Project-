# __init__.py 

## 1. variable: myobj
```
myobj = Flask(__name__)
```
Creates a flask object 
## 2. Flask Configurations:
```
myobj.config.from_mapping(
    SECRET_KEY = 'you-will-know',
    # location of sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    UPLOAD_FOLDER = 'md/markdown'
```
Sets object configurations for Flask object with enviroment variables. 
## 3. Login Manager:
```
login = LoginManager(myobj)
# right side is the function that's called to login users
login.login_view ='auth.login'
```
## 4. load_user():
```
'''
    parameter: (int) id 
    returns queried user 
'''
```