#!/usr/bin/python3

"""
A script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # add check to see if number of arguments is correct
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    # Establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # using format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            argv[4])
    cursor.execute(query)

    # Fetching all the results
    states = cursor.fetchall()

    # Display/print the results out
    for state in states:
        if state[1] == argv[4]:
            print(state)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
