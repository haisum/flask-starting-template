from core import app, db, connection

import pymongo
from pymongo.database import Database

app.config.from_object('core.config.TestingConfig')
"""
Load test database
"""
db = Database(connection, app.config["MONGODB_DATABASE"])

ctx = app.test_request_context('/')
ctx.push()

import tests.model_tests