#!/usr/bin/python3
import MySQLdb

# Connecting to Database
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

# Selecting Data using cursor
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database

# Print Data
query_rows = cur.fetchall()
for row in query_rows:
    print(row)

# Close connection
cur.close()
conn.close()
