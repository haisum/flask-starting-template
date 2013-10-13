import datetime
from core import app

@app.template_global()
def today():
	today = datetime.date.today()
	return dict(year=today.strftime("%Y"), day=today.strftime("%d"), month=today.strftime("%m") )