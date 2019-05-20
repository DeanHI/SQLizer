import sqlite3	
from flask_bcrypt import Bcrypt
from datetime import datetime
import bcrypt


def create_user_schema():
	sqlite_file = 'users_schema'	
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	columns_creation =					'CREATE TABLE IF NOT EXISTS Users \
										(CustomerID INTEGER default 1 PRIMARY KEY autoincrement,\
										Username TEXT default USERNAME NOT NULL,\
										FirstName TEXT default FN NOT NULL,\
										LastName TEXT default LN NOT NULL,\
										Password TEXT default MANNAME NOT NULL,\
										Email TEXT default USA NOT NULL,\
										DateOfBirth TEXT,\
										Country TEXT default COUNTRY,\
										State TEXT default NA,\
										IsAdmin NUMERIC default 0,\
										JoinTime TEXT NOT NULL,\
										NumOfVists INTEGER default 0,\
										CONSTRAINT username UNIQUE (Username),\
										CONSTRAINT email UNIQUE (Email))'

	c.execute(columns_creation)

	con.commit()
	
def insert_initial_values_users():
	"""This function is used to populate the users table in the initial schema with values of my own choosing"""
	sqlite_file = 'users_schema'
	con = sqlite3.connect(sqlite_file)
	c = con.cursor()
	
	users_value_template = 'INSERT INTO Users (Username, FirstName, LastName, Password,\
	Email, Country, IsAdmin, JoinTime) VALUES \
	(?, ?, ?, ?, ?, ?, ?, ?)'
	
	users_population = [
	("Freaker","Dan", "Tor", bcrypt.hashpw(b"dan123", bcrypt.gensalt()).decode("utf-8"), "dantor@yah.com", "Italy", 0, datetime.now()),
	("Porsche", "Guy", "Mor", bcrypt.hashpw(b"guy123", bcrypt.gensalt()).decode("utf-8"), "guymore@gm.com", "Germany", 0, datetime.now()),
	("Larp", "Darja", "Mik", bcrypt.hashpw(b"darja123", bcrypt.gensalt()).decode("utf-8"), "darja@yah.com", "UK", 0,  datetime.now()),
	("Nein", "Honda", "Fz", bcrypt.hashpw(b"honda123", bcrypt.gensalt()).decode("utf-8"), "honda@gm.com", "San Marino", 0, datetime.now()),
	("admin", "Dean", "H", bcrypt.hashpw(b"admin", bcrypt.gensalt()).decode("utf-8"), "dean123@yah.com", "Cyrpus", 1, datetime.now())
	]


	c.executemany( 'INSERT INTO Users (Username, FirstName, LastName, Password,\
	Email, Country, IsAdmin, JoinTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', users_population)
	con.commit()
	

def hash_password():
	pass
	

sqlite_file = 'users_schema'	
con = sqlite3.connect(sqlite_file)
c = con.cursor()
c.execute('SELECT * FROM SQLITE_MASTER')
if len(c.fetchall()) == 0:
	create_user_schema()	
	insert_initial_values_users()





		

	

