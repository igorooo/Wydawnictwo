import enum
from sqlalchemy import *
from sqlalchemy.orm import *
from engine import Base
from uzytkownicy import *
from objects import *


dostepnoscEnum = Enum('Platny', 'Darmowy')

autorstwo_table = Table(
    'Autorstwo', Base.metadata,
    Column('idAutor', Integer, ForeignKey('Autor.idAutor')),
    Column('idArtykul', Integer, ForeignKey('Artykul.idArtykul'))
)

class Artykul(Base):
    """Artykul"""
    __tablename__ = 'Artykul'
    id = Column("idArtykul", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    dataPublikacji = Column("DataPublikacji", Date, nullable=False)
    dostepnosc = Column("Dostepnosc", String(255), nullable=False)
    kontrybutor_id = Column('idKontrybutor', Integer, ForeignKey('Uzytkownik.idUzytkownik'), nullable=False)

    kontrybutor = relationship('Uzytkownik')
    tagi = relationship('Tag', backref='artykuly')

    wersja = relationship('Wersja', backref='wersja_backref')
    autorstwo = relationship('Autor', secondary='autorstwo_table', backref=backref('artykuly', lazy='dynamic'))

    def __init__(self, nazwa, dataPublikacji, dostepnosc, kontrybutor):
        self.nazwa = nazwa
        self.dataPublikacji = dataPublikacji
        self.dostepnosc = dostepnosc
        self.kontrybutor = kontrybutor

    def dodaj_tag(self, tagStr):
        tag = Tag(self, tagStr)
        self.tagi.append(tag)


class Wersja(Base):
    """Wersja"""
    __tablename__ = 'Wersja'
    id = Column("idWersja", Integer, primary_key=True)
    dataDodania = Column("DataDodania", Date, nullable=False)
    artykul_id = Column("idArtykul", ForeignKey('Artykul.idArtykul'), nullable=False)
    artykul = relationship('Artykul')
    tresc = Column("tresc", Binary, nullable=False)

    def __init__(self, nazwa, dataPublikacji, dostepnosc, kontrybutor):
        self.nazwa = nazwa
        self.dataPublikacji = dataPublikacji
        self.dostepnosc = dostepnosc
        self.kontrybutor = kontrybutor


class Tag(Base):
    """Tag"""
    __tablename__ = 'Tag'
    id = Column("idTag", Integer, primary_key=True)
    artykul_id = Column("idArtykul", ForeignKey('Artykul.idArtykul'), nullable=False)
    tag = Column("tag", String, nullable=False)

    artykul = relationship('Artykul')

    def __init__(self,artykul, tag):
        self.tag = tag
        self.artykul_id = artykul
