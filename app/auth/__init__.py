from flask import Blueprint #create a Blueprint instance auth

auth = Blueprint('auth',__name__)

from . import views