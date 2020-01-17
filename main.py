from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from engine import Base, engine
from uzytkownicy import Uzytkownik, Kontrybutor
from artykul import Artykul
from objects import *


# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine)

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()

# Let's create a user and add two e-mail addresses to that user.
#kontrybutor = Kontrybutor(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email')
kontrybutor = Kontrybutor(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email')
artykul = Artykul(nazwa='Artykul1', dataPublikacji='2015.01.01', dostepnosc='Platny', kontrybutor=kontrybutor)
recenzja = Recenzja(artykul=artykul, tresc=bytes('123', encoding='utf8'), recenzent=kontrybutor)


# Let's add the user and its addresses we've created to the DB and commit.
session.add(recenzja)
session.commit()
