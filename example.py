#!/usr/bin/python3
import MySQLdb

# Connect to database
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

# creating our cursor
c = db.cursor()

# Excuting Quiery
c.execute("""SELECT * FROM states ORDER BY id ASC""")

query_rows = c.fetchall()

for row in query_rows:
    print(row)




# conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
