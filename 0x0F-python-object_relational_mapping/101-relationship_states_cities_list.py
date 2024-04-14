#!/usr/bin/python3
"""City fetch module."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":
    usr, password, db = sys.argv[1:]
    engine = create_engine(f"""mysql+mysqldb://{usr}:
                           {password}@localhost:3306/{db}""")
    Session = sessionmaker(bind=engine)
    with Session() as session:
        states_and_cities = session.query(State)\
                                .outerjoin(City)\
                                .order_by(State.id, City.id)\
                                .all()
        for state in states_and_cities:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")
