import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:2face@localhost/blog'
    BLOG_API_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    POPULAR_QUOTE = 'http://quotes.stormconsultancy.co.uk/popular.json'
    SINGLE_QUOTE = ' http://quotes.stormconsultancy.co.uk/quotes/1.json'
    SECRET_KEY = 'test12345'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}

