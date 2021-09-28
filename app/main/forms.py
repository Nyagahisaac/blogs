from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class QuoteForm(FlaskForm):

    title = StringField('Quote title',validators=[Required()])
    quote = TextAreaField('Quote',validators=[Required()])
    submit = SubmitField('submit')
    

class AddBlog(FlaskForm):
    title = StringField('Title', validators =[Required()])
    content = TextAreaField('Content', validators = [Required()])
    submit = SubmitField('Post Blog')

class CommentForm(FlaskForm):

    comment = TextAreaField('Add a comment',validators = [Required()] )
    submit = SubmitField('Submit')          
    