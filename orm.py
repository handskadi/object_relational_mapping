#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import Session
from state_module import State, Base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

# Rest of your code remains the same...
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
        print("{}: {}".format(state.id, state.name))
session.close()
