from sqlalchemy import *
from sqlalchemy.orm import relationship
from engine import Base

class Uzytkownik(Base):
    """Klasa abstrakcyjna"""
    __tablename__ = 'Uzytkownik'
    id = Column("idUzytkownik", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    login = Column("Login", String(255), nullable=False)
    haslo = Column("Haslo", String(255), nullable=False)
    email = Column("Email", String(255), nullable=False)
    kontrybutor = relationship("Artykul")

    def __init__(self, nazwa, login, haslo, email):
        self.nazwa = nazwa
        self.login = login
        self.haslo = haslo
        self.email = email

class Kontrybutor(Uzytkownik):
    __mapper_args__ = {
        'polymorphic_identity':'Kontrybutor',
    }

class Recenzent(Kontrybutor):
    __mapper_args__ = {
        'polymorphic_identity':'Recenzent',
    }

class Redaktor(Recenzent):
    __mapper_args__ = {
        'polymorphic_identity':'Redaktor',
    }

class Administrator(Redaktor):
    __mapper_args__ = {
        'polymorphic_identity':'Administrator',
    }
