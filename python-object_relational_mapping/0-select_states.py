#!/usr/bin/python3

import MySQLdb
import sys

def main():
    # Get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
