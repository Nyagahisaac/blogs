from re import I
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField,BooleanField
from wtforms.validators import EqualTo, Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your Username',validators = [Required()])
    password = PasswordField('Password',validators = [Required()])
    submit =SubmitField('Sign Up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')
        
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That Username is taken')
        
class LoginForm(FlaskForm):
    username = StringField('Your username',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')