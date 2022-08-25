#!/usr/bin/python3
"""list all cities by state"""
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
    query = "SELECT cities.id,cities.name,states.name FROM cities \
             JOIN states ON cities.state_id=states.id WHERE states.name = %s \
             ORDER BY cities.id ASC"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    name_list = [i[1] for i in rows]
    print(', '.join(name_list))
