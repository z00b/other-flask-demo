'''The core of our flask app.'''

from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    '''Ensure that people feel very welcome.'''
    return "Hello, my fine other friend!"

@APP.route('/goodbye')
def goodbye():
    '''Returns a farewell message.'''
    return 'Ciao!'


if __name__ == "__main__":
    APP.run()
