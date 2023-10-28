from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, TextAreaField
from wtforms.validators import AnyOf, InputRequired, NumberRange, Optional, URL

"""
Form allow you to add a new pet
"""
class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Note")
    available = BooleanField("Available", default=True)
