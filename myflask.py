Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run()