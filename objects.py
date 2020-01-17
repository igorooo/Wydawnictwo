import enum
from sqlalchemy import *
from engine import Base
from artykul import *
from uzytkownicy import *


class Autor(Base):
    """Autor"""
    __tablename__ = 'Autor'
    id = Column("idAutor", Integer, primary_key=True)
    nazwisko = Column("Nazwisko", String(45), nullable=False)
    imie = Column("Imie", String(45), nullable=False)
    stopien = Column("Stopien", String(45), nullable=True)
    biografia = Column("Biografia", String(255), nullable=True)

    def __init__(self, nazwisko, imie, stopien, biografia):
        self.nazwisko = nazwisko
        self.imie = imie
        self.stopien = stopien
        self.biografia = biografia


class Zadanie(Base):
    """Zadanie"""
    __tablename__ = 'Zadanie'
    id = Column("idZadanie", Integer, primary_key=True)
    grupa = Column("Grupa", ForeignKey('Grupa.idGrupa'), nullable=False)
    zakres = Column("Zakres", String(45), nullable=False)
    artykul = Column("idArtykul", ForeignKey('Artykul.idArtykul'), nullable=False)
    wykonano = Column("Wykonano", Boolean, nullable=True)
    rezultat = Column("Rezultat", Boolean, nullable=True)

    def __init__(self, grupa, zakres, artykul):
        self.grupa = grupa
        self.zakres = zakres
        self.artykul = artykul


class Recenzja(Base):
    """Recenzja"""
    __tablename__ = 'Recenzja'
    id = Column("idRecenzja", Integer, primary_key=True)
    artykul = Column("idArtykul", ForeignKey('Artykul.idArtykul'), nullable=False)
    tresc = Column("tresc", Binary, nullable=False)
    recenzent = Column("Recenzent", ForeignKey('Recenzent.idUzytkownik'), nullable=False)

    def __init__(self, artykul, tresc, recenzent):
        self.artykul = artykul
        self.tresc = tresc
        self.recenzent = recenzent


weryfikanci_table = Table(
    'Weryfikanci', Base.metadata,
    Column('idUzytkownik', Integer, ForeignKey('Uzytkownik.idUzytkownik')),
    Column('idGrupa', Integer, ForeignKey('Grupa.idGrupa'))
)

zadania_table = Table(
    'Zadania', Base.metadata,
    Column('idZadanie', Integer, ForeignKey('Zadanie.idZadanie')),
    Column('idGrupa', Integer, ForeignKey('Grupa.idGrupa'))
)

class Grupa(Base):
    """Grupa"""
    __tablename__ = 'Grupa'
    id = Column("idGrupa", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(45), nullable=False)
    weryfikanci = relationship("Uzytkownik", secondary=weryfikanci_table)
    zadania = relationship("Zadanie", secondary=zadania_table)


    def __init__(self, nazwa, weryfikanci, zadania):
        self.nazwa = nazwa
        self.weryfikanci = weryfikanci
        self.zadania = zadania

def Kategoria(Base):
    """Kategoria"""
    __tablename__ = 'Kategoria'
    id = Column("idKategoria", Integer, primary_key=True)
    nazwa = Column("idArtykul", String(45), nullable=False)
    opis = Column("idArtykul", String(255), nullable=False)


    def __init__(self, nazwa, opis):
        self.nazwa = nazwa
        self.opis = opis
