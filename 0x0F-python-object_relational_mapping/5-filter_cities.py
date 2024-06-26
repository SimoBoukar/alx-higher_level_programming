#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name FROM cities JOIN states\
        ON cities.state_id = states.id WHERE states.name\
        LIKE BINARY %(name)s ORDER BY cities.id ASC", {'name': sys.argv[4]}
        )
    query_rows = cur.fetchall()
    print(", ".join([row[1] for row in query_rows]))
    cur.close()
    conn.close()
