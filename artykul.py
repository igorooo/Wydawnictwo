import enum
from sqlalchemy import *
from engine import Base


dostepnoscEnum = Enum('Platny', 'Darmowy')

class Artykul(Base):
    """Artykul"""
    __tablename__ = 'Artykul'
    id = Column("idArtykul", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    dataPublikacji = Column("DataPublikacji", Date, nullable=False)
    dostepnosc = Column("Dostepnosc", String(255), nullable=False)
    kontrybutor = Column("Kontrybutor", ForeignKey('Kontrybutor.idUzytkownik'), nullable=True)

    def __init__(self, nazwa, dataPublikacji, dostepnosc, kontrybutor):
        self.nazwa = nazwa
        self.dataPublikacji = dataPublikacji
        self.dostepnosc = dostepnosc
        self.kontrybutor = kontrybutor


class Wersja(Base):
    """Wersja"""
    __tablename__ = 'Wersja'
    id = Column("idWersja", Integer, primary_key=True)
    dataDodania = Column("DataDodania", Date, nullable=False)
    artykul = Column("idArtykul", ForeignKey('Artykul.idArtykul'), nullable=False)
    tresc = Column("tresc", Binary, nullable=False)

    def __init__(self, nazwa, dataPublikacji, dostepnosc, kontrybutor):
        self.nazwa = nazwa
        self.dataPublikacji = dataPublikacji
        self.dostepnosc = dostepnosc
        self.kontrybutor = kontrybutor
