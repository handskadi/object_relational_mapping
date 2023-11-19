#!/usr/bin/python3
import MySQLdb

# Connection parameters
host = "localhost"
user = "root"
password = "root"
database = "my_db"
port = 3306
charset = "utf8"

# Establish a connection
conn = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=database, charset=charset)

# Create a cursor object to interact with the database
cur = conn.cursor()

#  Execute SQL queries using the cursor : Insert Query
cur.execute("INSERT INTO states (name, population) VALUES (%s, %s)", ("Morocco", 40000000))

# Commit the changes
conn.commit()

# Close connection
cur.close()
conn.close()
