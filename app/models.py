
from token import COMMENT

# from app.main.forms import CommentForm
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from sqlalchemy.sql import func
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model): #create 'User' class to help in creating new users
   
    __tablename__ = 'users' #__tablename__ variable allows us to give the tables in our db proper names

    id = db.Column(db.Integer,primary_key = True) #create columns using db.Column class which represents a single column.db.Integer specifies data to be stored
    username = db.Column(db.String(255)) #db.String class specifies data to be a string with 255 characters maximum
    email = db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='pitch', lazy='dynamic')
    comments = db.relationship("Comment", backref="user", lazy = "dynamic")


    @property #@property decorator creates a write only class property 'password'
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self): #repr method easens debugging of our application
        return f'User {self.username}'


class Pitch(db.Model):
    #List of pitches

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vote = db.Column(db.Integer)
    comments = db.relationship("Comment", backref="pitches", lazy = "dynamic")
    vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")

    def save_pitch(self):
        ''' Save the pitches '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    # display pitches

    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches


class Comment(db.Model):
    #User comments

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    feedback = db.column(db.String)
    time_posted = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    
    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = COMMENT.query.order_by(CommentForm.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment


class Category(db.Model):
    #pitch Categories
    
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    category_name= db.Column(db.String)

    # save pitches
    def save_category(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


  
#votes
class Votes(db.Model):
    '''
    class to model votes 
    '''
    
    __tablename__='votes'

    id = db.Column(db. Integer, primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Votes.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
        return votes