from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from objects import *
from engine import *


# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine)

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()



kontrybutor = Kontrybutor(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email')
add_object_to_db(kontrybutor)

artykul = Artykul(nazwa='Artykul1', dataPublikacji='2015.01.01', dostepnosc='Platny', kontrybutor=kontrybutor.id)
add_object_to_db(artykul)
# recenzja = Recenzja(artykul=artykul, tresc=bytes('123', encoding='utf8'), recenzent=kontrybutor)


