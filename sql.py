# sql.py - Create a SQLite3 table and populate it with data.

import sqlite3

# Create a new db if it doesn't exist already
with sqlite3.connect("blog.db") as connection:

	# Get cursor
	cursor = connection.cursor()

	# Create table
	cursor.execute("""CREATE TABLE posts
		(title TEXT, post TEXT)
		""")

	# Insert dummy data
	cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	cursor.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	cursor.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')