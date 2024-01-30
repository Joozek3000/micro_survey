from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question_text = StringField('Question', validators=[DataRequired()])
    question_type = SelectField('Type', choices=[('text', 'Text'), ('multiple-choice', 'Multiple Choice')])

class CreateSurveyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    questions = FieldList(FormField(QuestionForm), min_entries=1)
    submit = SubmitField('Create Survey')
