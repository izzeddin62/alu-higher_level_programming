#!/usr/bin/python3
"""list all states"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name)
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
