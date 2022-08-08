
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


# create sql db instance
db = SQLAlchemy()

# create SQL Model
class Users(db.Model):
    '''
        User class for signing up
    '''
    
    def __init__(self):
        
        self.id = db.Column(db.Integer, primary_key=True)
        self.name = db.Column(db.String(200), nullable=False)
        self.email = db.Column(db.String(120), nullable=False, unique=True)
        self.data_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    # On user creation submit information to DB
    
 

    def __repr__(self):
        return '<Name %r> % self.name'