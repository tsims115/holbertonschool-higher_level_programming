#!/usr/bin/python3
"""Start link class to table in database and fetch states
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    flag = 0
    for instance in session.query(State).order_by(State.id):
        if sys.argv[4] == instance.name:
            flag = 1
            print("{}".format(instance.id))
    if flag == 0:
        print("Not found")
