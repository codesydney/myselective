from flask import render_template, flash, redirect
from app import app
from .forms import MainForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = MainForm()
    return render_template('mainform.html',
                            title='Main Form',
                            form=form)