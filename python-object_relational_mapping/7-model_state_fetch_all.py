#!/usr/bin/python3
"""list all states"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all()
        print(state.id, state.name)
    

