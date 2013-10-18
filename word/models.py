
class Word(object):
	"""
	Word model for manipulating words collection
	structure = {
		'lang': unicode,
		'local': unicode,
		'phrase' : unicode,
		'translation': unicode,
		'views' : [{
			'user_id' : unicode,
			'date_viewed' : datetime,
		}],
		'views_count' : int,
		'details' : [{
			'description' : unicode,
			'examples' : [{
				'local' : unicode,
				'phrase' : unicode,
				'translation' : unicode,
			}],
			'likes' : [{
				'user_id' : unicode,
				'date_liked' : datetime,
			}],
			'dislikes' : [{
				'user_id' : unicode,
				'date_disliked' : datetime,
			}],
			'likes_count' : int,
			'dislikes_count' : int,
			'status' : int,
			'date_detailed' : datetime,
			'user_nick' : unicode,
			'user_id' : unicode
		}],
		'date_added' : datetime,
		'tags' : list,
		'status' : int,
		'user_id' : unicode,
	}
	"""
	def __init__(self, db):
		self.db = db

	__collection__ = 'words'

	STATUS = {
		"approved" : 1,
		"pending" : 0,
		"rejected" : -1,
	}

	def insert(self, data):
		self.db[self.__collection__].insert(data)

	def validate(self, data):
		pass	


class Language(object):
	"""
	Language model for manipulating language collection
	structure = {
		"language" : unicode,
		"status" : Word.STATUS["approved"]
 	}
	"""
	def __init__(self, db):
		self.db = db

	__collection__ = 'users'

	def insert(self, data):
		self.db[self.__collection__].insert(data)

	def validate(self, data):
		pass