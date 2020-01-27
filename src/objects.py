from engine import *
from uzytkownicy import Recenzent


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
    grupa_id = Column("idGrupa", Integer, ForeignKey('Grupa.idGrupa'), nullable=False)
    zakres = Column("Zakres", String(45), nullable=False)
    artykul_id = Column("idArtykul", Integer, ForeignKey('Artykul.idArtykul'), nullable=False)
    wykonano = Column("Wykonano", Boolean, nullable=True)
    rezultat = Column("Rezultat", Boolean, nullable=True)

    artykul = relationship('Artykul')
    grupa = relationship('Grupa')

    def __init__(self, grupa, zakres, artykul):
        self.grupa = grupa
        self.zakres = zakres
        self.artykul = artykul

    def wykonaj(self, rezultat: bool):
        if self.wykonano:
            return false
        self.rezultat = rezultat
        return true

    def ponow(self):
        if not self.wykonano:
            return false
        z = Zadanie(self.grupa, self.zakres, self.artykul)
        session.add(z)
        session.commit()
        session.flush()
        return true


class Recenzja(Base):
    """Recenzja"""
    __tablename__ = 'Recenzja'
    id = Column("idRecenzja", Integer, primary_key=True)
    artykul_id = Column("idArtykul", Integer, ForeignKey('Artykul.idArtykul'), nullable=False)
    tresc = Column("tresc", String(255), nullable=False)
    recenzent_id = Column("idRecenzent", ForeignKey('Uzytkownik.idUzytkownik'), nullable=False)

    artykul = relationship('Artykul')
    recenzent = relationship('Uzytkownik')

    def __init__(self, artykul, tresc, recenzent):
        self.artykul = artykul
        self.tresc = tresc
        self.recenzent = recenzent


weryfikanci_table = Table(
    'Weryfikanci', Base.metadata,
    Column('idUzytkownik', Integer, ForeignKey('Uzytkownik.idUzytkownik')),
    Column('idGrupa', Integer, ForeignKey('Grupa.idGrupa'))
)


class Grupa(Base):
    """Grupa"""
    __tablename__ = 'Grupa'
    id = Column("idGrupa", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(45), nullable=False)

    weryfikanci = relationship("Uzytkownik", secondary=weryfikanci_table, backref=backref('grupy_weryfikacji', lazy='dynamic'))
    zadania = relationship('Zadanie', backref='grupa_weryfikacjyna')

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def dodaj_weryfikanta(self, weryfikant: Recenzent):
        self.weryfikanci.append(weryfikant)
        session.add(self)
        session.commit()
        session.flush()

    def podaj_sklad(self):
        q = session.query(Recenzent, weryfikanci_table).join(Recenzent.id).filter(weryfikanci_table.idGrupa == self.id)
        output = []
        for r, w in q:
            output.append(r.nazwa)
        return output


class Kategoria(Base):
    """Kategoria"""
    __tablename__ = 'Kategoria'
    id = Column("idKategoria", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(45), nullable=False)
    opis = Column("Opis", String(255), nullable=False)

    artykul = relationship('Artykul')

    def __init__(self, nazwa, opis):
        self.nazwa = nazwa
        self.opis = opis
