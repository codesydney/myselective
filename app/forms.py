from flask_wtf import Form
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SubmitField, HiddenField
from wtforms import validators
from wtforms.validators import DataRequired
from werkzeug.datastructures import MultiDict

class MainForm(Form):
	SchoolAssessmentTitle = StringField("School Assessment")
	School_English = IntegerField('English', [validators.Required("Please enter your English school assessment.")],render_kw={"placeholder": "","size":"10"})	
	School_Maths = IntegerField('Mathematics', [validators.Required("Please enter your Maths school assessment.")],render_kw={"placeholder": "","size":"10"})	
	ExaminationScoresTitle = StringField("Examination Scores")
	ExaminationScores_English = IntegerField('English', [validators.Required("Please enter your English exam score.")],render_kw={"placeholder": "","size":"10"})	
	ExaminationScores_Maths = IntegerField('Mathematics', [validators.Required("Please enter your Maths exam score.")],render_kw={"placeholder": "","size":"10"})
	ExaminationScores_GA = IntegerField('General Ability', [validators.Required("Please enter your GA exam score.")],render_kw={"placeholder": "","size":"10"})
	ExaminationScores_Writing = IntegerField('Writing', [validators.Required("Please enter your Writing exam score.")],render_kw={"placeholder": "","size":"10"})
	HomeAddressTitle = StringField("My Home Address")		
	HomeAddress = StringField('Home Address', [validators.Required("Please enter your Home address.")],render_kw={"placeholder": "Type in your home address","id":"geocomplete","size":"90"})	
	HomeLat = HiddenField(render_kw={"id":"home_lat"})	
	HomeLng = HiddenField(render_kw={"id":"home_lng"})		
	Submit1 = SubmitField('Submit',render_kw={"size":"90"})	    

class ResultForm(Form):
    Submit2 = SubmitField('Try again',render_kw={"size":"90"})	 