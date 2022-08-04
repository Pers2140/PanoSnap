
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

# Create Form Class
class NamerForm(FlaskForm):
    '''
        Gets user's form submission 
    '''
    name = None
    email = None
    name = StringField("Hey whats your name", validators=[DataRequired()])
    email = StringField("Hey whats your email", validators=[DataRequired()])
    submit = SubmitField("Submit")