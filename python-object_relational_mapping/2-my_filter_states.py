#!/usr/bin/python3
"""Shebang script"""

import MySQLdb
import sys

if __name__ == "__main__":
    """The main entry point of the script."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(sys.argv[4]))

    query_rows = cursor.fetchall()

    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    cursor.close()
    db.close()