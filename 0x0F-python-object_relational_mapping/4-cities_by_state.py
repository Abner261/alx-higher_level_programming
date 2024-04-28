#!/usr/bin/python3

"""
A script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username, mysql password
and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # createing a cursor object to execute SQL queries
    cursor = db.cursor()

    # executing the cursor to retrieve cities sorted by id
    city_query = """SELECT cities.id, cities.name, states.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query)

    # fetching all the results
    cities = cursor.fetchall()

    # display/print them out
    for city in cities:
        print(city)

    # closing the cursor and database connection
    cursor.close()
    db.close()
