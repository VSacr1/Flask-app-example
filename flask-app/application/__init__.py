from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder="templates")

# Sets up your database. We are using SQLAlchemy's sqlite. 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

# imports the routes.py from application. 
from application import routes
