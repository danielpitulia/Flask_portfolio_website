from app import app
from flask import render_template, url_for

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/publictransport')
def publictransport():
	return render_template('publictransport.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')

@app.route('/unitcircle')
def chat():
	return render_template('unitcircle.html')
