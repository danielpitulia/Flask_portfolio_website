from app import app
from flask import render_template, url_for, request
from timetables import get_timetables
from token_vasttrafik import get_token
from forms import EmailForm
from flask_mail import Mail, Message
import datetime

date = datetime.datetime.now().strftime("%c")


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
	date = datetime.datetime.now().strftime("%c")
	form = EmailForm()
	if form.validate_on_submit():
		mail = Mail(app)
		msg = Message(form.message.data, sender = form.email.data, recipients = ['daniel@dpitulia.com'])
		msg.body = form.message.data
		mail.send(msg)
		sent_message = "Your message has been sent."
		return render_template('index.html', title='HOME', date=date, css="styles_index", form=form, sent_message=sent_message)
	else:
		return render_template('index.html', title='HOME', date=date, form=form, css="styles_index")

@app.route('/publictransport', methods=['GET', 'POST'])

def publictransport():
# If the user enters a search (POST method), request data from Västtrafik.
# Else, render an empty table.
	if "token" not in locals():
		token = get_token()

	if request.method == 'POST':
		date = datetime.datetime.now().strftime("%c")
		stop_input = request.form['stop_input']
		timetable_and_stop = get_timetables(token, stop_input)
		departures_zip = timetable_and_stop[0]
		stop_name = timetable_and_stop[1]
		return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input = stop_input, css="styles_publictransport", stop_name=stop_name)

	elif request.method == 'GET':

		line,delta,destination = "", "", ""
		date = datetime.datetime.now().strftime("%c")
		departures_zip=zip(line, delta, destination)
		stop_input=""
		return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input = stop_input, css="styles_publictransport", stop_name="")

@app.route('/chat')
def chat():
	date = datetime.datetime.now().strftime("%c")
	return render_template('chat.html', title='CHAT', date=date, css="styles_chat")

@app.route('/unitcircle')
def unitcircle():
	date = datetime.datetime.now().strftime("%c")
	return render_template('unitcircle.html', title='UNIT CIRCLE', date=date, css="styles_unitcircle", js_online="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=AM_CHTML", js_static="js/unitcircle/unitcircle.js")

@app.route('/raspberry')
def raspberry():
	date = datetime.datetime.now().strftime("%c")
	return render_template('raspberry.html', title='RASPBERRY', date=date, css="styles_3dprint")
