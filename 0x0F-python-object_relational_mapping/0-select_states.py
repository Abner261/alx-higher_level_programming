#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
