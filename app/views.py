from flask import render_template, flash, redirect, request, url_for
from app import app, db, models
from .forms import MainForm, ResultForm
from math import sin, cos, sqrt, atan2
from flask_bootstrap import Bootstrap

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = MainForm()
	resultform = ResultForm()
	
	if form.validate_on_submit() and form.Submit1.data:
		School_English = form.School_English.data
		form.School_English.data = ''
       
		School_Maths = form.School_Maths.data
		form.School_Maths.data = ''
        
		ExaminationScores_English = form.ExaminationScores_English.data
		form.ExaminationScores_English.data = ''
        
		ExaminationScores_Maths = form.ExaminationScores_Maths.data
		form.ExaminationScores_Maths.data = ''

		ExaminationScores_GA = form.ExaminationScores_GA.data
		form.ExaminationScores_GA.data = ''

		ExaminationScores_Writing = form.ExaminationScores_Writing.data
		form.ExaminationScores_Writing.data = ''
        
		Total_English = (School_English + (ExaminationScores_English * 0.667 + ExaminationScores_Writing * 0.333)) / 2
		Total_Maths = (School_Maths + ExaminationScores_Maths) / 2
		Total_GA = ExaminationScores_GA
		Total_Score = Total_English + Total_Maths + Total_GA
        
		HomeAddress = form.HomeAddress.data
		HomeLat = form.HomeLat.data
		HomeLng = form.HomeLng.data		
		
		#If no address inputted, geocode defaults to 100 Market St, Sydney
		if not HomeLat:
			HomeLat = "-33.8704510"
			HomeLng = "151.2087600"
			HomeAddress = "Invalid home address. Distance is computed from 100 Market St, Sydney NSW 2000"
		
		schools = models.School.query.filter(models.School.entryscore <= Total_Score).order_by(models.School.entryscore.desc()).all()
		R = 6373.0
		
		school_list = []
		
		for school in schools:
			dlon = school.schoollng - float(HomeLng)	
			dlat = school.schoollat - float(HomeLat)			
			a = sin(dlat / 2)**2 + cos(float(HomeLat)) * cos(float(school.schoollat)) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))
			distance = round((R * c) / 100,2) 			
			selected_fields=[school.schoolname,school.entryscore,school.website,distance]
			school_list.append(selected_fields)
		
			
		return render_template('result.html',
								resultform=resultform,
								School_English=School_English,
								School_Maths=School_Maths,
								ExaminationScores_English=ExaminationScores_English,
								ExaminationScores_Maths=ExaminationScores_Maths,
								ExaminationScores_GA=ExaminationScores_GA,
								ExaminationScores_Writing=ExaminationScores_Writing,                                								
								Total_Score=int(Total_Score),
								HomeAddress=HomeAddress,
								HomeLat=HomeLat,
								HomeLng=HomeLng,
								schools=schools,
								school_list=school_list)								
								
	elif resultform.validate_on_submit() and resultform.Submit2.data:	
         return redirect(url_for('index'))
	else:		
	    return render_template('mainform.html',
                                form=form)