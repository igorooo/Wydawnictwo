from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost:3306/OWydawnictwo')


class Uzytkownik(Base):
    """Klasa abstrakcyjna"""
    __tablename__ = 'Uzytkownik'
    id = Column("idUzytkownik", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    login = Column("Login", String(255), nullable=False)
    haslo = Column("Haslo", String(255), nullable=False)
    email = Column("Email", String(255), nullable=False)

    def __init__(self, nazwa, login, haslo, email):
        self.nazwa = nazwa
        self.login = login
        self.haslo = haslo
        self.email = email

class Kontrybutor(Uzytkownik):
    __mapper_args__ = {
        'polymorphic_identity':'Kontrybutor',
    }
    id_pracownika = Column("idPracownika", Integer)

    def __init__(self, nazwa, login, haslo, email, id_pracownika):
        super(Kontrybutor, self).__init__(nazwa, login, haslo, email)
        self.id_pracownika = id_pracownika


# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine)

# Creates a new session to the database by using the engine we described.
Session = sessionmaker(bind=engine)
session = Session()

# Let's create a user and add two e-mail addresses to that user.
#kontrybutor = Kontrybutor(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email')
kontrybutor = Kontrybutor(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email', id_pracownika=1)
uzytkownik = Uzytkownik(nazwa='Nazwa', login='Login', haslo='Haslo', email='Email')


# Let's add the user and its addresses we've created to the DB and commit.
session.add(uzytkownik)
session.add(kontrybutor)
session.commit()
