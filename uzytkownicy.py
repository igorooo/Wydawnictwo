from sqlalchemy import *
from engine import Base

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
