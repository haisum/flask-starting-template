
class User(object):
	"""
	User model for manipulating users collection
	structure = {
		"nick" : unicode,
		"fullname" : "",
		"email" : "",
		"favourites" : [],
		"roles" : [],
		"reputation" : int,
		"logins" : [{
			'ip' : unicode,
			'time' : datetime,
			'timezone' : unicode
		}],
		"about" : unicode
	}
	"""
	def __init__(self, db):
		self.db = db

	__collection__ = 'users'

	def insert(self, data):
		self.db[self.__collection__].insert(data)

	def validate(self, data):
		pass	

