from app import app
from flask import render_template, url_for
import datetime
from publictransport import get_timetables



@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html', title='HOME', date=date)

@app.route('/publictransport')
def publictransport():
	date = datetime.datetime.now().strftime("%c")
	departures_zip = get_timetables("Rävekärr")
	return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip)

@app.route('/chat')
def chat():
	return render_template('chat.html', title='CHAT', date=date)

@app.route('/unitcircle')
def unitcircle():
	return render_template('unitcircle.html', title='UNIT CIRCLE', date=date)

@app.route('/raspberry')
def raspberry():
	return render_template('raspberry.html', title='RASPBERRY', date=date)
