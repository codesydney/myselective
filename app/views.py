from flask import render_template, flash, redirect, request
from app import app
from .forms import MainForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MainForm()
    
    #if request.method == 'POST':
    if form.validate_on_submit():
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
        
        return render_template('result.html',
                                form=form,
                                School_English=School_English,
                                School_Maths=School_Maths,
                                ExaminationScores_English=ExaminationScores_English,
                                ExaminationScores_Maths=ExaminationScores_Maths,
                                ExaminationScores_GA=ExaminationScores_GA,
                                ExaminationScores_Writing=ExaminationScores_Writing,
                                Total_Score=Total_Score)
    else:    
        return render_template('mainform.html',
                                form=form)