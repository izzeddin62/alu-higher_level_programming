#!/usr/bin/python3
"""list all states matching name argument(safe)"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state = argv[4]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (state,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
