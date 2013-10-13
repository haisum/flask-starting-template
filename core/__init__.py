from flask import Flask
from word import bp_word


app = Flask(__name__, static_folder="../static", template_folder="../layouts")
app.config.from_object('core.config.DevelopmentConfig')

app.register_blueprint(bp_word)

from core.context_processors import *