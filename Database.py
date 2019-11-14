# DISREGARD, WILL USE FOR FUTURE 

import sqlite3

connectionObject = sqlite3.connect("users.db")

cursor = connectionObject.cursor()

#createTable = "CREATE TABLE users(email varchar(32))"

#cursor.execute(createTable)

insertValues = "INSERT INTO users values('test')"

cursor.execute(insertValues)

queryTable = "SELECT * from users"

queryResults = cursor.execute(queryTable)

recs = cursor.fetchall()

print(recs)