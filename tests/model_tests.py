import os
import unittest
from tests import app, db, ctx
from bson.dbref import DBRef
from word.models import Word
from datetime import datetime

class ModelWordTestCase(unittest.TestCase):

	def setUp(self):
		user_data = {
			
		}
		db.words.remove()
	
	def test_insert(self):
		data = {
		'lang': "en",
		'local': "Japanese shit",
		'pronunciation' : "another something",
		'meaning': "some random shit",
		'details' : [{
			'description' : "used in random stuff",
			'examples' : [{
				'local' : "hello",
				'pronunciation' : "wello",
				'meaning' : "tello",
			}],
			'status' : Word.STATUS["approved"],
			'date_detailed' : datetime.utcnow().isoformat()
		}],
		'date_added' : datetime.utcnow().isoformat(),
		'tags' : ["random shit"],
		'status' : Word.STATUS["approved"],
		}
		
		word = Word(db)
		word.insert(data)

		word = db.words.find_one()
		self.assertEqual(word["lang"], "en")
		self.assertEqual(word["status"], 1)
		self.assertEqual(len(word["details"]), 1)
		self.assertEqual(len(word["details"][0]["examples"]), 1)
		self.assertEqual(len(word["tags"]), 1)

	def tearDown(self):
		db.words.remove()

if __name__ == '__main__':
	unittest.main()