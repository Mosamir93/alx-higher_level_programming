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
        cities = session.query(City)\
                        .order_by(City.id)\
                        .all()
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")
