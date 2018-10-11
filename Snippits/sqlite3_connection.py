#!/usr/bin/env python

# Import
import sqlite3
import time

database="/tmp/sqlite3.db"

def main():

	Fname = "Firstname"
	Lname = "LastName"

	sqlcon, sqlcur = sql_connection()

	# Try to create the table, failing assuming table exists
	try:
		sqlcur.execute("""CREATE TABLE Contacts (Time INTEGER, Fname TEXT, Lname TEXT)""")
	except:
		print("Table exists")

	# Sample write
	sqlcur.execute("""INSERT INTO Contacts (Time, Fname, Lname) VALUES (%d,'%s','%s');""" % (get_time(),Fname,Lname))

	# Sample read and print results
	results = sqlcur.execute("""SELECT * from Contacts""")
	print('| %15s | %15s | %15s |' % ("Time", "FirstName", "LastName"))
	print( "-" * 55)
	for row in results:
		print('| %15s | %15s | %15s |' % row)
	print("-" * 55)

	# Close connection
	sql_diconnection(sqlcon, sqlcur)


def get_time():
	# Return epoch milliseconds
	epochmilli = int(round(time.time() * 1000))
	return epochmilli

def sql_connection():
	sqlcon = sqlite3.connect(database)
	sqlcur = sqlcon.cursor()

	return sqlcon, sqlcur

def sql_diconnection(connection, cursor):
	# Commit and close
	connection.commit()
	cursor.close()
	connection.close()


if __name__ == "__main__":
	main()

