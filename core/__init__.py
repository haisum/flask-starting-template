"""
Main file from which app will start
First it imports all blueprints
createts a app object and registers blueprints
then imports all additional modules that require app object
"""
from flask import Flask
#import all blueprints
from word import bp_word

"""
Naming default templates folder to layouts because it will contain base templates and layouts,
real content will be inside <module_name>/templates folder which will extend templates in layouts folder
"""
app = Flask(__name__, static_folder="../static", template_folder="../layouts")

app.register_blueprint(bp_word)

"""
Config can be either of 
DevelopmentConfig
ProductionConfig
TestingConfig
"""
app.config.from_object('core.config.DevelopmentConfig')


import core.context_processors
import core.loggers