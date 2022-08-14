
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
import sqlite3


# create sql db instance
# db = SQLAlchemy()

# create SQL Model
class User():
    '''
        User class for signing up
    '''
    
    def __init__(self,user):
        
        self.first_name = user['first_name'] 
        self.last_name = user['last_name']
        self.username= user['username']
        self.password = user['password']
        self.email = user['email']
    
        # On user creation submit information to DB
        # Connect to database
        db_conn = sqlite3.connect('test.db') 
        
        # Cursor to interact with DB
        c = db_conn.cursor()
        
        # submit pano 
        c.execute("INSERT INTO users ('username','password','email') VALUES (?,?,?)", ( self.username, self.username, self.email))
        print('New user submitted to DB new ')
        
        # close connection to DB
        db_conn.commit()
        db_conn.close()
    
 

    def __repr__(self):
        return '<Name %r> % self.name'