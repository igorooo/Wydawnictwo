from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

Base = declarative_base()

engine = create_engine('sqlite:///Wydawnictwo', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def add_object_to_db(object):
    session.add(object)
    session.commit()
