from sqlalchemy.orm import Session

from root import *
from root.db_models import *
from sqlalchemy_utils import database_exists, create_database

if __name__ == '__main__':
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Creating admin
    session = Session(engine)
    session.add(User('Admin', 'admin', 'admin'))
    session.commit()
    session.close()
