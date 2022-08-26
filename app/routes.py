from app import app
from flask import render_template, url_for
import datetime

date = datetime.datetime.now().strftime("%c")

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html', title='HOME', date=date)

@app.route('/publictransport')
def publictransport():
	return render_template('publictransport.html', title='TIMETABLE APP', date=date)

@app.route('/chat')
def chat():
	return render_template('chat.html', title='CHAT', date=date)

@app.route('/unitcircle')
def unitcircle():
	return render_template('unitcircle.html', title='UNIT CIRCLE', date=date)

@app.route('/raspberry')
def raspberry():
	return render_template('raspberry.html', title='RASPBERRY', date=date)
