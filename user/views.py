from flask import render_template, abort, url_for, request, redirect, session
from jinja2 import TemplateNotFound
from flask import Blueprint
from core import app, oid

import json

bp_user = Blueprint('bp_user', __name__, template_folder="templates")

@bp_user.route("/login")
@oid.loginhandler
def login():
	"""
	show login page
	"""
	try:
		if request.args.get("openid_identifier") is not None:
			openid = request.args.get("openid_identifier")
			return oid.try_login(openid, ask_for=['email', 'fullname',
												  'nickname', 'language', 'image', 'timezone'])
		else:
			return render_template("login.html", next=oid.get_next_url(), error = oid.fetch_error())
	except TemplateNotFound:
		app.logger.error("template user/login.html not found")
		abort(404)

@oid.after_login
def create_or_login(resp):
	app.logger.debug(json.dumps(resp))
	#session['openid'] = resp.identity_url

	#user = User.query.filter_by(openid=resp.identity_url).first()
	# if user is not None:
	#     flash(u'Successfully signed in')
	#     g.user = user
	#     return redirect(oid.get_next_url())
	return redirect(url_for('user_profile', next=oid.get_next_url(),
							name=resp.fullname or resp.nickname,
							email=resp.email))

@bp_user.route("/profile")
def user_profile():
	return json.dumps(request.args)

app.register_blueprint(bp_user)