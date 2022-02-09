from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,RadioField,SubmitField,SelectField,ValidationError
from wtforms.validators import Required

#Pitch Form
class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Sales'), ('2', 'Product'), ('3', 'Secrets'), ('4', ('Confessions'), ('5', 'Reviews'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')

#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

class CategoryForm(FlaskForm):
    name = StringField('Pitch', validators=[Required()])
    title = TextAreaField('Pitch')
    submit = SubmitField()