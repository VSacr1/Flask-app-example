# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Todos, Lists
from application.forms import TodoForm, ListForm

#READ 
@app.route('/', methods=['POST', 'GET'])
def index():
    todos = Todos.query.all()
    return render_template('index.html', title="To do List", todos=todos)

#CREATE 
@app.route('/add', methods=['POST','GET'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        todos = Todos(
            tasks = form.tasks.data
        )
       
        db.session.add(todos)
        print("This is to test the submit")
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title="Add a new Task", form=form)

#UPDATE 

#DELETE