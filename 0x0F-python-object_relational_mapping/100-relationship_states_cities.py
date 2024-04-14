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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_city = City(name="San Francisco")
        new_state = State(name="California", cities=[new_city])
        session.add(new_state)
        session.add(new_city)
        session.commit()
