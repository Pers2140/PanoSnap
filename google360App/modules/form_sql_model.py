
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create sql db instance
db = SQLAlchemy()

# create SQL Model
class Users(db.Model):
    '''
        User class for signing up
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r> % self.name'