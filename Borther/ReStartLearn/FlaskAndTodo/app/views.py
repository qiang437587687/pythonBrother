from ReStartLearn.FlaskAndTodo.app import app
from flask import render_template

from ReStartLearn.FlaskAndTodo.app.models import Todo


@app.route('/')
def index():
    return render_template('FlaskToindex.html', todos=Todo)





