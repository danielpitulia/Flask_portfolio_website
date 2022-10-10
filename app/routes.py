from app import app
from flask import render_template, url_for, request, flash, redirect
from timetables import get_timetables
from token_vasttrafik import get_token
from forms import EmailForm, SearchForm
from flask_mail import Mail, Message
import datetime

date = datetime.datetime.now().strftime("%c")

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    js_static = "index.js"
    topBanner = "HOME"
    date = datetime.datetime.now().strftime("%c")
    form = EmailForm()
    if form.validate_on_submit():
        return redirect('/')

    #if request.method == 'POST':
    #    name = request.form['name']
    #    email = request.form['e-mail']
    #    message = request.form['message']
#
#        if not name:
#            flash('Name is required!')
#        elif not email:
#            flash('E-mail is required!')
#        elif not message:
#            flash('Message is required!')
#        else:
#            return redirect(url_for('index'))

    return render_template('index.html', title='Web projects', date=date, css="styles_index", topBanner = topBanner, js_static=js_static, form=form)
    #if form.validate_on_submit():
    #    mail = Mail(app)
    #    msg = Message(form.message.data, sender=form.email.data, recipients=['daniel@dpitulia.com'])
    #    msg.body = form.message.data
    #    mail.send(msg)
    #    sent_message = "Your message has been sent."
    #    return render_template('index.html', title='D. Pitulia', date=date, css="styles_index", form=form, sent_message=sent_message, topBanner = topBanner, js_static=js_static)
    #else:
    #    return render_template('index.html', title='Web Projects', date=date, form=form, css="styles_index", topBanner = topBanner, js_static=js_static)


@app.route('/publictransport', methods=['GET', 'POST'])
def publictransport():
    form = SearchForm()
    # Get token from Västtrafik for authentication if it hasn't been done
    if "token" not in locals():
    	token = get_token()

    if form.validate_on_submit():
        # Get timetables based on user's search
        date = datetime.datetime.now().strftime("%c")
        stop_input = form.search.data
        timetable_and_stop = get_timetables(token, stop_input)
        departures_zip = timetable_and_stop[0]
        stop_name = timetable_and_stop[1]
        return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input=stop_input, css="styles_publictransport", stop_name=stop_name, form=form)
    else:
        # Render an empty form for first visit
        line, delta, destination = "", "", ""
        date = datetime.datetime.now().strftime("%c")
        departures_zip = zip(line, delta, destination)
        stop_input = ""
        return render_template('publictransport.html', title='TIMETABLE APP', date=date, departures_zip=departures_zip, stop_input=stop_input, css="styles_publictransport", stop_name="", form=form)


@app.route('/unitcircle')
def unitcircle():
    date = datetime.datetime.now().strftime("%c")
    return render_template('unitcircle.html', title='UNIT CIRCLE', date=date, css="styles_unitcircle", js_online="https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=AM_CHTML", js_circle="unitcircle.js")


@app.route('/raspberry')
def raspberry():
    date = datetime.datetime.now().strftime("%c")
    return render_template('raspberry.html', title='RASPBERRY', date=date, css="styles_3dprint")
