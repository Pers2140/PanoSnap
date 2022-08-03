from flask import Flask, render_template, flash, request

from modules.Form import *
from modules.sqlModel import *

"""
    To have live server update on change set FLASK vars
    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
"""

# create instance
app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SECRET_KEY"] = "password"


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
    print (request.json)
    return render_template("index.html")
    
# create name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    email = None
    form = NamerForm()
    
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
        flash('Form Submitted Successfully')
    return render_template("name.html", name=name, email=email, form=form)

if __name__ == '__main__':
   app.run(debug = True)