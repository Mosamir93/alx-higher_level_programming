#!/usr/bin/python3
"""State list module."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usr, password, db_name = sys.argv[1:]
    engine_conn = """mysql+mysqldb://{}:{}
                @localhost:3306/{}""".format(usr, password, db_name)
    engine = create_engine(engine_conn)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = "New Mexico"
            session.commit()
