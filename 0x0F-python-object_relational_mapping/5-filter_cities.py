#!/usr/bin/python3
"""List all cities module."""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    states_name = sys.argv[4]

    with MySQLdb.connect(host="localhost",
                         port=3306,
                         user=usr,
                         passwd=passwd,
                         db=db_name) as db:
        cursor = db.cursor()
        query = """SELECT cities.name
                    FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    where states.name = %s
                    ORDER BY cities.id"""
        cursor.execute(query, (states_name,))
        cities = cursor.fetchall()
        for i, city in enumerate(cities):
            print(city[0], end='')
            if i < len(cities) - 1:
                print(", ", end='')
            else:
                print()
