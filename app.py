from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_cors import CORS, cross_origin   
from flask_bcrypt import Bcrypt
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import json

from modules.form import *
# from modules.favpano import *
# from modules.User import *

"""
    To have live server update on change set FLASK vars
    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
"""
db = SQLAlchemy()


# create sql db instance
# db = SQLAlchemy()

# create SQL Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    panos = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
# create instance
app = Flask(__name__)
# create sql db instance
db.init_app(app)         
with app.app_context():
    db.create_all()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gbkwzleyaglirn:078915c822e17cbb4c2cb86fe7d8ff000b9f15cc5d3a7fbe2049bbb7810b057b@ec2-34-234-240-121.compute-1.amazonaws.com:5432/d38mm771ie34mq'
app.config["SECRET_KEY"] = "078915c822e17cbb4c2cb86fe7d8ff000b9f15cc5d3a7fbe2049bbb7810b057b"
# load flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# add bcrypt to app
bcrypt = Bcrypt(app)


    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create index route
@app.route("/")
@cross_origin()
def index():
    return render_template("map.html")

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
    # favpano(user_fav)
    usertoupdate = User.query.filter_by(username=current_user.username).first()
    usertoupdate.panos += "|" + str(user_fav)
    # usertoupdate.panos += "|"+"{'latLng': {'lat': 40.75822369999999, 'lng': -73.98540849999999}, 'shortDescription': 'Times Square','description': 'Times Square','pano': 'CAoSK0FGMVFpcFAxRUtQcG1mZWZGMU4xS1hGZ3RxeTRLbm9COTk1UVZoV0NocTg.', 'profileUrl': '//maps.google.com/maps/contrib/104359050004655709521'}"
    print(usertoupdate.panos)
    db.session.commit()
    return render_template("index.html")

# endpoint to delete favpano
@app.route("/rmfav", methods=["GET", "POST"])
def deletefav():
    if request.method == 'POST':
        print ("someone posted something to remove")
    user_ans = request.json
    
    print (int(user_ans)+1)
    posToDel = int(user_ans)+1
    
    usertoupdate = User.query.filter_by(username=current_user.username).first()
    panoslist = usertoupdate.panos.split("|")
   
    # check if last postion in array
    if (int(posToDel)+1 == len(panoslist)):
        todelpano = "|%s"%(panoslist[int(posToDel)])
        updatedpanos = str(usertoupdate.panos).replace(str(todelpano),"")
    else:
        todelpano = "|%s|"%(panoslist[int(posToDel)])
        updatedpanos = str(usertoupdate.panos).replace(str(todelpano),"|")
    
    usertoupdate.panos = updatedpanos
    print (updatedpanos)
    db.session.commit()
    return render_template("index.html")

# create signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,
                        panos="{'latLng': {'lat': 40.75822369999999, 'lng': -73.98540849999999}, 'shortDescription': 'Times Square','description': 'Times Square','pano': 'CAoSK0FGMVFpcFAxRUtQcG1mZWZGMU4xS1hGZ3RxeTRLbm9COTk1UVZoV0NocTg.', 'profileUrl': '//maps.google.com/maps/contrib/104359050004655709521'}",
                        password=hashed_password,
                        email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        print ("New user %s added with pass %s" %(new_user.username,hashed_password))
        return redirect(url_for('login'))
    else:
        print("Adding user failed")
                        
    return render_template('signup.html', form=form)

# create login page
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        current_user.user_data = "panos and shit"
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    print(eval(current_user.panos))
    userdata = current_user.panos
    # print (type(userdata))
    return render_template('user.html',username=current_user.username, userdata=eval(userdata.replace("|",",")))

if __name__ == '__main__':
   app.run(debug = True)