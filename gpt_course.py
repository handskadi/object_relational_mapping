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

try:
    # Begin the transaction
    conn.begin()
    
    #  Execute SQL queries using the cursor
    cur.execute("SELECT * FROM states ORDER BY id ASC") 

    # Fetch all rows
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    
    # Commit the transaction
    conn.commit()

except Exception as e:
    # Rollack the transcation if an error occurs
    conn.rollback()
    print(f"Error: {e}")

finally:
    # Close connection
    cur.close()
    conn.close()
