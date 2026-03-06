#!/usr/bin/python3
"""Script that lists all states with a specific name from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = BINARY '{}' "
        "ORDER BY states.id ASC".format(state_name)
    )

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
