#!/usr/bin/python3
"""Shebang  script"""

import sys
import MySQLdb

if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    cur.close()
    db.close()
