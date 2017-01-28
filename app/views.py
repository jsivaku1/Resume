from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Jay'}
    return render_template('index.html')

@app.route('/fareresult')
def fareresult():
    return render_template('fareresult.html')


@app.route('/tripresult')
def tripresult():
    return render_template('tripresult.html')
