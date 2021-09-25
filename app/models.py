from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(UserMixin,db.Model):
    __tablename__= 'users'

    

    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


class Quote:
    '''
    Blog class to define blog objects
    '''
    def __init__(self,author,quote):
        self.id = id
        self.author = author
        self.quote = quote

        
