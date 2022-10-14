# Links the database with your routes, by creating input forms. 

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

from application.models import Todos, Lists 

class TodoForm(FlaskForm):
    tasks = StringField("Task")
    submit = SubmitField("Submit")

class ListForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField("Submit")