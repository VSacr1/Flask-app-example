# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Todos, Lists
from application.forms import TodoForm, ListForm

@app.route('/', methods=['POST', 'GET'])
def index():
    todos = Todos.query.all()
    return render_template('index.html', title="To do List", todos=todos)