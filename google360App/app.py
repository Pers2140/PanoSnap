from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from sqlalchemy import true
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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

# create sql db instance
db = SQLAlchemy(app)

# create SQL Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r> % self.name'

# create Form Class
class NamerForm(FlaskForm):
    name = StringField("Hey whats your name", validators=[DataRequired()])
    email = StringField("Hey whats your email", validators=[DataRequired()])
    submit = SubmitField("Submit")


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
