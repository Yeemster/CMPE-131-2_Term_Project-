from myapp import create_app
from myapp import myobj
myobj = create_app()

if __name__ == '__main__':
    myobj.run(debug=True)
