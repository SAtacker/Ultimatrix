from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, RadioField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    datetime = StringField('DateTime', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    treat = RadioField('Treat', choices=[('value', "Yes, i'll give treat :)"),
                                         ('value_two', "Sorry, I won't give treat :(")])
    submit = SubmitField('Post')