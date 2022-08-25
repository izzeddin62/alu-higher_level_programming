#!/usr/bin/python3
"""list all states with name equal to the fourth argument"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db_name)
    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State)\
        .filter_by(name=state_name).order_by(State.id).first()
    if state:
        print(str(state.id))
    else:
        print('Not Found')
