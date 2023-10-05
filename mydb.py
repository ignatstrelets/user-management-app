# using mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'ubuntu',
	passwd = ''
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE itransition_django_app")

print("Database successfully created")
