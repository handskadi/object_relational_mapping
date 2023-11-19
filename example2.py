#!/usr/bin/python3
import MySQLdb

# Connect to database
db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

# creating our cursor
c = db.cursor()

# Excuting Quiery
#c.execute("CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")

try:
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
except MySQLdb.Error as e:
    try:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    except IndexError:
        print("MySQL Error: %s" % str(e))

# Print results in comma delimited format
for row in rows:
    for col in row:
        print( "%s," % col)

# Print the number of selected rows
numrows = len(rows)
print("\n")
print("Selected %s rows" % numrows)

# close Database
c.close()
db.close()


# conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
