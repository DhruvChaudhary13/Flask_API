from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)


# Database configuration used to interact with database through python object
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/App'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import routes after initializing app and db
from .routes import *



