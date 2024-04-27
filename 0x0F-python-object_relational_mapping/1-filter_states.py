#!/usr/bin/python3

"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql password
and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # Executing the cursor to retrieve states sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetching all the results
    states = cursor.fetchall()

    # Display/print them out
    for state in states:
        if state[1][0] == 'N':
            print(state)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
