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

