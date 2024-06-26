#!/usr/bin/python3
"""
prints all City objects
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
