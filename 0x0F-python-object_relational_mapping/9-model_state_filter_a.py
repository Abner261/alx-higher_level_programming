#!/usr/bin/python3
"""A Script to list all State objects that contain the letter 'a'
   from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create connection to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and display State objects containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
