from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import config_options
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

#Initialising Flask Bootstrap
bootstrap = Bootstrap()
#initialising database
db = SQLAlchemy()
#Initialising email
mail = Mail()
#uploading photos
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    #initialising application
    app = Flask(__name__)

    #Setting up configuration
    app.config.from_object(config_options [config_name])
    app.config.from_pyfile('config.py')

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    #configure Uploadset
    configure_uploads(app,photos)
    
    #Register the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Register the auth blueprint
    from.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #Import simplemde
    from flask_simplemde import SimpleMDE
    simple = SimpleMDE()
    simple.init_app(app)

    return app