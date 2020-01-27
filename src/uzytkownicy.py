from artykul import Artykul, Wersja
from engine import *
from objects import Autor, Grupa, Zadanie, Kategoria


class Uzytkownik(Base):
    """Klasa abstrakcyjna"""
    __tablename__ = 'Uzytkownik'
    id = Column("idUzytkownik", Integer, primary_key=True)
    nazwa = Column("Nazwa", String(255), nullable=False)
    login = Column("Login", String(255), nullable=False)
    haslo = Column("Haslo", String(255), nullable=False)
    email = Column("Email", String(255), nullable=False)
    type_id = Column("Type", Integer)

    artykul = relationship('Artykul', backref='kontrybutor_backref')
    recenzja = relationship('Recenzja', backref='kontrybutor_backref')

    __mapper_args__ = {
        'polymorphic_on': type_id,
        'polymorphic_identity': 'Uzytkownik'
    }

    def __init__(self, nazwa, login, haslo, email):
        self.nazwa = nazwa
        self.login = login
        self.haslo = haslo
        self.email = email

    # TODO: Implementacja metod Użytkownika


class Kontrybutor(Uzytkownik):
    __mapper_args__ = {
        'polymorphic_identity':'Kontrybutor',
    }

    def dodaj_autora(self, a: Autor):
        q = session.query(Autor).filter(Autor.imie == a.imie).filter(Autor.nazwisko == a.nazwisko)
        if not session.query(q.exists()).scalar():
            session.add(a)
            session.commit()
            session.flush()
            return true
        else:
            return false

    def dodaj_artykul(self, a: Artykul):
        q = session.query(Artykul).filter(Artykul.nazwa == a.nazwa)
        if not session.query(q.exists()).scalar():
            session.add(a)
            session.commit()
            session.flush()
            return true
        else:
            return false

    def dodaj_wersje(self, w: Wersja):
        # TODO: Implementacja metody

        return false

    def sklad_grupy(self, g: Grupa):
        return g.podaj_sklad()


class Recenzent(Kontrybutor):
    __mapper_args__ = {
        'polymorphic_identity':'Recenzent',
    }

    def stworz_zadanie(self, a: Artykul, g: Grupa, zakres: str):
        z = Zadanie(g, zakres, a)
        session.add(z)
        session.commit()
        session.flush()

    def oznacz_zadanie(self, z: Zadanie, rezultat: bool):
        z.wykonaj(rezultat)

    def wystaw_recenzje(self, a: Artykul, tresc):
        # TODO: Implementacja metody

        return false

    def pobierz_artykul(self, a: Artykul):
        # TODO: Implementacja metody

        return false


class Redaktor(Recenzent):
    __mapper_args__ = {
        'polymorphic_identity':'Redaktor',
    }

    def scal_autorow(self, a1: Autor, a2: Autor):
        #TODO: Implementacja metody

        return false

    def dodaj_grupe(self, g: Grupa):
        q = session.query(Grupa).filter(Grupa.nazwa == g.nazwa)
        if not session.query(q.exists()).scalar():
            session.add(g)
            session.commit()
            session.flush()
            return true
        else:
            return false

    def dodaj_do_grupy(self, g: Grupa, r: Recenzent):
        g.dodaj_weryfikanta(r)

    def dodaj_kategorie(self, k: Kategoria):
        q = session.query(Kategoria).filter(Kategoria.nazwa == k.nazwa)
        if not session.query(q.exists()).scalar():
            session.add(k)
            session.commit()
            session.flush()
            return true
        else:
            return false

    def zmien_status(self, a: Artykul, status):
        # TODO: Implementacja metody

        return false


class Administrator(Redaktor):
    __mapper_args__ = {
        'polymorphic_identity':'Administrator',
    }

    def dodaj_recenzenta(self, r: Recenzent):
        q = session.query(Recenzent).filter(Recenzent.nazwa == r.nazwa)
        if not session.query(q.exists()).scalar():
            session.add(r)
            session.commit()
            session.flush()
            return true
        else:
            return false

    def dodaj_redaktoraa(self, r: Redaktor):
        q = session.query(Redaktor).filter(Redaktor.nazwa == r.nazwa)
        if not session.query(q.exists()).scalar():
            session.add(r)
            session.commit()
            session.flush()
            return true
        else:
            return false
