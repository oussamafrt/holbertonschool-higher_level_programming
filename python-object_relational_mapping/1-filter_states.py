#!/usr/bin/oythin3

import MySQLdb
import sys

def main():
    """The main entry point of the script."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
