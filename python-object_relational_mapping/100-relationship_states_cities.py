#!/usr/bin/python3
"""create state and city"""
from relationship_state import Base, State
from relationship_city import City
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
    state = State(name='California')
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
