#!/usr/bin/python3
"""List all cities module."""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    with MySQLdb.connect(host="localhost",
                         port=3306,
                         user=usr,
                         passwd=passwd,
                         db=db_name) as db:
        cursor = db.cursor()
        query = """SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY id"""
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            print(city)
