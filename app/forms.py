from flask_wtf import Form
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired

class MainForm(Form):
    SchoolAssessmentTitle = StringField("School Assessment")
    School_English = IntegerField('English', [validators.Required("Please enter your English School Assessment.")])
    School_Maths = IntegerField('Mathematics', [validators.Required("Please enter your Maths School Assessment.")])
    
    ExaminationScoresTitle = StringField("Examination Scores")
    ExaminationScores_English = IntegerField('English', [validators.Required("Please enter your English Exam Score.")])
    ExaminationScores_Maths = IntegerField('Maths', [validators.Required("Please enter your Maths Exam Score.")])
    ExaminationScores_GA = IntegerField('GA', [validators.Required("Please enter your GA Exam Score.")])
    ExaminationScores_Writing = IntegerField('Writing', [validators.Required("Please enter your Writing Exam Score.")])
    
    submit = SubmitField('Run')
