from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class QuoteForm(FlaskForm):

    title = StringField('Quote title',validators=[Required()])
    quote = TextAreaField('Quote',validators=[Required()])
    submit = SubmitField('submit')
    
          
        