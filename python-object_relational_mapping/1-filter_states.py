#!/usr/bin/python3
"""list all states starting with N"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id ASC'
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
