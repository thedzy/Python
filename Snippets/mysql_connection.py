#!/usr/bin/env python3

# pip3 install mysql-connector==2.1.4
import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

# DB connection inforation
hostname = 'db.example.com'
username = 'databaseuser'
password = 'databasepass'
database = 'example'

print("Using mysql.connector")

try:
	# Initilaise database
	mysqlconn = mysql.connector.connect(host=hostname, user=username, passwd=password, database=database)
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print("Connection error %s" % err)
else:
	print("Connected")
	# Connect
	cursor = mysqlconn.cursor()

	# Query
	query = "SELECT COUNT(*) from table1"
	cursor.execute(query)

	count = cursor.fetchone()[0]

	# Close connections
	cursor.close()
	mysqlconn.close()

	print(count)
