
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

# Create Form Class
class NamerForm(FlaskForm):
    '''
        Gets user's form submission 
    '''
   
    username = StringField("Hey whats your username", validators=[DataRequired()])
    password = StringField("Hey whats your password", validators=[DataRequired()])
    email = StringField("Hey whats your email", validators=[DataRequired()])
    submit = SubmitField("Submit")
    