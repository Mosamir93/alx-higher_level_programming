#!/usr/bin/python3
"""Get all states starting with N module."""
import MySQLdb
import sys

if __name__ == "__main__":
    """Script to get all states starting with N."""
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=usr,
                         passwd=passwd,
                         db=db_name)

    cursor = db.cursor()
    query = """SELECT * FROM states
                   WHERE name LIKE BINARY %s
                   ORDER BY id"""
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
