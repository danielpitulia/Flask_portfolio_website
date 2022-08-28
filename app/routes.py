from app import app
from flask import render_template, url_for, request
from timetables import get_timetables
from token_vasttrafik import get_token

import datetime

date = datetime.datetime.now().strftime("%c")
token = get_token()

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html', title='HOME', date=date)

@app.route('/publictransport', methods=['GET', 'POST'])

def publictransport():

	if request.method == 'POST':
		stop_input = request.form['stop_input']
		departures_zip = get_timetables(token, stop_input)
		return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input = stop_input)

	elif request.method == 'GET':
		line,delta,destination = "", "", ""
		departures_zip=zip(line, delta, destination)
		stop_input=""
		return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input = stop_input)

@app.route('/chat')
def chat():
	return render_template('chat.html', title='CHAT', date=date)

@app.route('/unitcircle')
def unitcircle():
	return render_template('unitcircle.html', title='UNIT CIRCLE', date=date)

@app.route('/raspberry')
def raspberry():
	return render_template('raspberry.html', title='RASPBERRY', date=date)
