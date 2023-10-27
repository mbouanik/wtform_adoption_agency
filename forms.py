from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, TextAreaField
from wtforms.validators import InputRequired 


class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    note = TextAreaField("Note")
    available = BooleanField("Available", default=True)
