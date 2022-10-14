# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from asyncio import Task
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
    # This points to TodoForm
    form = TodoForm()
    # Checks that we have clicked the submit button
    if form.validate_on_submit():
        # the variable tasks becomes what is put on the form 
        # todos becomes what we are going to be adding to the database
        todos = Todos(
            tasks = form.tasks.data
        )
        # This performs the add to database
        db.session.add(todos)
        # This commits those changes
        db.session.commit()
        # This one redirects to the index functions url
        return redirect(url_for('index'))
    # Otherwise return the template of add.html
    return render_template('add.html', title="Add a new Task", form=form)

#UPDATE 

#DELETE
@app.route('/delete/<int:tid>')
def delete(tid):
    # Collecting the task we want to delete based on its id
    tasks = Todos.query.get(tid)
    # deleting this item from the database
    db.session.delete(tasks)
    # committing this change
    db.session.commit()
    # returning the url in the index function. 
    return redirect(url_for('index'))