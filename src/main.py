from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

Base.metadata.create_all(engine)


user = Uzytkownik('User', 'Login', 'Haslo', 'Email')
autor = Autor('NazwiskoAutora', 'ImieAutora', '9000', 'biografia')
kategoria = Kategoria('kategoria1', 'opis kategorii')

session.add_all([user, autor, kategoria])
session.commit()

artykul = Artykul('Artykul1', date(2010, 2, 1), 'Platny', user)
session.add(artykul)
session.commit()

recenzja = Recenzja(artykul, 'recenzja artykulu', user)
wersja = Wersja(date(2010, 10, 1), artykul, 'tresc arttykulu')

session.add_all([recenzja, wersja])
session.commit()

grupa = Grupa('Grupa1')
session.add(grupa)
session.commit()

zadanie = Zadanie(grupa, 'zakres zadania', artykul)
session.add(zadanie)
session.commit()

# Tablice asoscjacyjne

artykul2 = Artykul('Artykul2', date(2010, 2, 1), 'Platny', user)
session.add(artykul2)
session.commit()

artykul.referowanie.append(artykul2)
artykul.autorstwo.append(autor)
artykul.dodaj_tag('Tag1') #gotowa metoda
grupa.weryfikanci.append(user)

session.commit()



