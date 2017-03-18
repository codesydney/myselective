from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields.html5 import EmailField


class MainForm(Form):
    SchoolAssessmentTitle = TextField("School Assessment")
    School_English = IntegerField('English', [validators.Required("Please enter your English School Assessment.")])
    School_Maths = IntegerField('Mathematics', [validators.Required("Please enter your Maths School Assessment.")])
    
    ExaminationScoresTitle = TextField("Examination Scores")
    ExaminationScores_English = IntegerField('English', validators=[DataRequired()])
    ExaminationScores_Maths = IntegerField('Maths', validators=[DataRequired()])
    ExaminationScores_GA = IntegerField('GA', validators=[DataRequired()])
    ExaminationScores_Writing = IntegerField('Writing', validators=[DataRequired()])
    
    submit = SubmitField('Run')
    
