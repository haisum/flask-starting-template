from flask import render_template, abort, url_for
from jinja2 import TemplateNotFound
from word import bp_word

@bp_word.route("/")
def index():
	# try:
		return render_template("home.html")
	# except TemplateNotFound:
	# 	abort(404)
