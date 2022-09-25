from flask import Flask
from config import Config

app = Flask(__name__)
application = app
app.config.from_object(Config)
app.secret_key = "test-string-for-development"

from app import routes
