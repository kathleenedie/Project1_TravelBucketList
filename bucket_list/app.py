from flask import Flask
    #import flask and render template

app = Flask(__name__)

from controllers import cities_controller

if __name__=='__main__':
    app.run(debug=True)