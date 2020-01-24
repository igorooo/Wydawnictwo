from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()
engine = create_engine('sqlite:///Wydawnictwo')
Session = sessionmaker(bind=engine)
session = Session()

def add_object_to_db(object):
    session.add(object)
    session.commit()
