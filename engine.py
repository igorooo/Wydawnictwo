from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost:3306/OWydawnictwo')
