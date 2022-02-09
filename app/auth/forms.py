from flask_wtf import FlaskForm  #import flaskform class from flask_wtf extension
from wtforms import StringField,PasswordField,ValidationError,BooleanField,SubmitField #import input fields to facilitate user input
from wtforms.validators import Required,Email,EqualTo #import validators.Email validator validates input follows proper email structure and EqualTo helps in comparing the two passwords inputs
from ..models import User 


#Registration Input Fields
class RegistrationForm(FlaskForm): #Creating Registration form class
    email = StringField('Your Email Address',validators=[Required(),Email()]) #input field email passing in required and email validators 
    username = StringField('Username',validators=[Required()]) #input username field
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message="Passwords must match")]) #input password field
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()]) #input password confirm field
    submit = SubmitField('Sign Up')


    #Creating methods. #Import ValidationError from wtforms
    def validate_email(self,data_field): #validate_email takes in the data field,checks our database to confirm there is no user registered with that email address.
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with this email') #If user is found a ValidationError is raised and the error message passed in is displayed. The form is not submitted.

    def validate_username(self,data_field): #validate_username checks if the username is unique and raises a ValidationError if another user with a similar username is found
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
#If a method inside a form class begins with validate it is considered as a validator and is run with the other validators for that input field

#Login Input Fields 
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    #input fields for the users email,password and a boolean to confirm whether the user wants to be logged out after the session