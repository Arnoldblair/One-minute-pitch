
import os #import os module that allows our app to interact with the OS dependent functionality

class Config:
    
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'one-min-pitch'
    SENDER_EMAIL ='munenearnoldblair@gmail.com'
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
    
    # WTF_CSRF_SECRET_KEY="a csrf secret key"



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blair:admin123@localhost/pitches'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}