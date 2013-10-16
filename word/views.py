from flask import render_template, abort, url_for, current_app
from jinja2 import TemplateNotFound
from word import bp_word

@bp_word.route("/")
def home():
	"""
	business logic for home page
	"""
	try:
		return render_template("home.html")
	except TemplateNotFound:
		current_app.logger.error("template word/home.html not found")
		abort(404)

@bp_word.route("/add", methods=["GET"])
def show_add_form():
	"""
	Shows add word form
	"""
	try:
		return render_template("add_word.html")
	except TemplateNotFound:
		current_app.logger.error("template word/add_word.html not found")
		abort(404)