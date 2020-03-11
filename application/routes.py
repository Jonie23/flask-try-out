from flask import render_template, redirect, url_for
from application import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

