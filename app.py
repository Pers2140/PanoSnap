from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

from modules.form import *
from modules.favpano import *
from modules.User import *

"""
    To have live server update on change set FLASK vars
    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
"""

# create instance
app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = "password"
# load flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# add bcrypt to app
bcrypt = Bcrypt(app)
# create sql db instance
db = SQLAlchemy(app)           

    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create index route
@app.route("/")
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
    user_fav["username"] = "Darius"
    favpano(user_fav)
    print (user_fav['pano'])
    
    return render_template("index.html")


# create signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password,email=form.email.data)
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
        user.user_data = "panos and shit"
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
    print(user)
    return render_template('user.html',username=current_user.username)

if __name__ == '__main__':
   app.run(debug = True)