from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager #import the LoginManager class from the flask-login extension

login_manager = LoginManager()
login_manager.session_protection = 'strong' #login_manager.session_protection attribute provides different security levels and by setting it to strong will monitor the changes in a user's request header and log the user out
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy() #create db instance

def create_app(config_name):
    
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


    return app