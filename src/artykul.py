from engine import *


dostepnoscEnum = Enum('Platny', 'Darmowy')
statusEnum = Enum('Recenzja', 'Weryfikacja', 'Redakcja', 'Publikacja', 'Archiwizacja')

autorstwo_table = Table(
    'Autorstwo', Base.metadata,
    Column('idAutor', Integer, ForeignKey('Autor.idAutor')),
    Column('idArtykul', Integer, ForeignKey('Artykul.idArtykul'))
)

referowanie_table = Table(
    'Referowanie', Base.metadata,
    Column('idArtykulReferujacy', Integer, ForeignKey('Artykul.idArtykul')),
    Column('idArtykulReferowany', Integer, ForeignKey('Artykul.idArtykul'))
)


class Wersja(object):
    pass


class Artykul(Base):
    """Artykul"""
    __tablename__ = 'Artykul'
    id = Column("idArtykul", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    dataPublikacji = Column("DataPublikacji", Date, nullable=True)
    dostepnosc = Column("Dostepnosc", String(255), nullable=False)
    kontrybutor_id = Column('idKontrybutor', Integer, ForeignKey('Uzytkownik.idUzytkownik'), nullable=False)
    kategoria_id = Column('idKategoria', Integer, ForeignKey('Kategoria.idKategoria'), nullable=True)
    status = Column('Status', String(255), nullable=True)

    kontrybutor = relationship('Uzytkownik')
    tagi = relationship('Tag', backref='artykuly')
    zadanie = relationship('Zadanie', backref='artykul_zadanie')
    recenzja = relationship('Recenzja', backref='artykul_recenzowany')
    wersja = relationship('Wersja', backref='wersjonowany_artykul')
    autorstwo = relationship('Autor', secondary=autorstwo_table, backref=backref('artykuly', lazy='dynamic'))
    referowanie = relationship('Artykul', secondary=referowanie_table,
                               primaryjoin=id == referowanie_table.c.idArtykulReferowany,
                               secondaryjoin=id == referowanie_table.c.idArtykulReferujacy,
                               backref=backref('referowany', lazy='dynamic'))

    def __init__(self, nazwa, dataPublikacji, dostepnosc, kontrybutor):
        self.nazwa = nazwa
        self.dataPublikacji = dataPublikacji
        self.dostepnosc = dostepnosc
        self.kontrybutor = kontrybutor

    def dodaj_tag(self, tagStr):
        tag = Tag(self, tagStr)
        self.tagi.append(tag)

    def dodaj_wersje(self, w: Wersja):
        # TODO: Implementacja metody

        return false


class Wersja(Base):
    """Wersja"""
    __tablename__ = 'Wersja'
    id = Column("idWersja", Integer, primary_key=True)
    dataDodania = Column("DataDodania", Date, nullable=False)
    artykul_id = Column("idArtykul", Integer, ForeignKey('Artykul.idArtykul'), nullable=False)
    tresc = Column("tresc", String(255), nullable=False)

    artykul = relationship('Artykul')

    def __init__(self,  dataDodania, artykul, tresc):
        self.dataDodania = dataDodania
        self.artykul = artykul
        self.tresc = tresc


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
