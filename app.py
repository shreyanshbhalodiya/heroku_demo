from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Learning Heroku in Praxis"


@app.route('/someendpoints')
def firstendpoint():
    return "this is my first path on heroku"
