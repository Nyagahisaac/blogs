from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required


class QuoteForm(FlaskForm):

    title = StringField('Quote title',validators=[Required()])
    quote = TextAreaField('Quote',validators=[Required()])
    submit = SubmitField('submit')