
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
import sqlite3


# create sql db instance
db = SQLAlchemy()

# create SQL Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
 
