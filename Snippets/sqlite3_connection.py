#!/usr/bin/env python

# Import
import sqlite3
import time

DATABASE = "/tmp/sqlite3.db"


def main():
	first_name = "Firstname"
	last_name = "LastName"

	sqlcon, sqlcur = sql_connection()

	# Try to create the table, failing assuming table exists
	try:
		sqlcur.execute("""CREATE TABLE Contacts (Time INTEGER, Fname TEXT, Lname TEXT)""")
	except:
		print("Table exists")

	# Sample write
	sqlcur.execute("""INSERT INTO Contacts (Time, Fname, Lname) VALUES (%d,'%s','%s');""" % (get_time(), first_name, last_name))

	# Sample read and print results
	results = sqlcur.execute("""SELECT * from Contacts""")
	print('| %15s | %15s | %15s |' % ("Time", "FirstName", "LastName"))
	print("-" * 55)
	for row in results:
		print('| %15s | %15s | %15s |' % row)
	print("-" * 55)

	# Close connection
	sql_diconnection(sqlcon, sqlcur)

def get_time():
	"""
	Return epoch milliseconds
	:return: (Int) Epoch
	"""
	epochmilli = int(round(time.time() * 1000))
	return epochmilli

def sql_connection():
	"""
	Create an SQL connection
	:return: (Object) SQL Connection, (Object) SQL Cursors
	"""
	sqlcon = sqlite3.connect(DATABASE)
	sqlcur = sqlcon.cursor()

	return sqlcon, sqlcur

def sql_diconnection(connection, cursor):
	"""
	Commit and close connection
	:param connection: (Object) SQL Connection
	:param cursor: (Object) SQL Cursors
	:return:
	"""
	connection.commit()
	cursor.close()
	connection.close()


if __name__ == "__main__":
	main()

