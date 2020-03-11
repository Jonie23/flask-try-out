from flask import render_template, redirect, url_for, Blueprint
from application import app

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

