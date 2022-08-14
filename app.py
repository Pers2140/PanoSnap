from flask import Flask, render_template, flash, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from dotenv import load_dotenv

import sqlite3
import os

load_dotenv()

from modules.form import *
from modules.favpano import *
from modules.User import *
map_key= os.getenv("KEY")

"""
    To have live server update on change set FLASK vars
    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
"""

# Connect to database
db_conn = sqlite3.connect('test.db') 

# Cursor to interact with DB
c = db_conn.cursor()

# Create a Table
# c.execute(""" 
#           CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, 
          
#           username TEXT,
#           password TEXT,
#           Email TEXT
         
#           )
          
#           """)

# c.execute("INSERT INTO panos ('username','description','latlng','pano','profile_url') VALUES (?,?,?,?,?)", ('ZeusDaddy','test','test','password123','Bigz@gmail.com'))
# c.execute("INSERT INTO users ('username','password','email') VALUES (?,?,?)", ('BigDadaZ','password123','Bigz@gmail.com'))

c.execute("SELECT * FROM users")
print(c.fetchall())
# execute / commit command

db_conn.commit()
db_conn.close()



# create instance
app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SECRET_KEY"] = "password"
# load flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

flask = os.getenv("FLASK_APP")
# create index route
@app.route("/")
def index():
    print (map_key)
    return render_template("map.html", map_key=map_key)

# create user route
@app.route("/user/<name>")
def user(name,email):
    # pass ^ name to user.html
    return render_template("user.html", name=name, email=email)

# endpoint to post users favorite Pano locations
@app.route("/fav", methods=["GET","POST"])
def fav():
    if request.method == 'POST':
        print ("someone posted something")
        
    user_fav = request.json
    user_fav["username"] = "Darius"
    favpano(user_fav)
    print (user_fav['pano'])
    
    return render_template("index.html")


# create signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = None
    password = None
    email = None
    form = NamerForm()
    
    # Validate Form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        User({"first_name":"none","last_name":"testing","username":username,"password":password,"email":email})
        form.username.data = ''
        form.password.data = ''
        form.email.data = ''
        flash('Form Submitted Successfully')
    return render_template("signup.html", username=username, password=password, email=email, form=form)

# create login page
@app.route("/login", methods=["GET", "POST"])
def login():
    username = None
    password = None
    form = NamerForm()
    
    # Validate Form
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        print("submit button pressed")
        print ('%s has logged in Successfully' % (username))
        
    return render_template("login.html", username=username, password=password, form=form)

if __name__ == '__main__':
   app.run(debug = True)