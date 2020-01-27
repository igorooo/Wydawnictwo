from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

"""
    Plik na wszystkie inserty do bazy
"""

user = Kontrybutor('Tomasz Kowalski', 'kowalski', '1234', 'email@email.com')
session.add(user)
session.commit()

artykul = Artykul('Ekonomia Polski przed II wojną światową', date(2010, 2, 1), 'Darmowy', user)
artykul1 = Artykul('Polski przemysł XX wieku', date(2012, 3, 6), 'Platny', user)
artykul2 = Artykul('Sieci neuronowe w medycynie', date(2012, 3, 6), 'Darmowy', user)
session.add_all([artykul, artykul1, artykul2])
session.commit()

artykul.dodaj_tag("ekonomia")
artykul.dodaj_tag("historia")

artykul1.dodaj_tag("ekonomia")
artykul1.dodaj_tag("historia")
artykul1.dodaj_tag("technologia")
artykul1.dodaj_tag("przemysł")

artykul2.dodaj_tag("informatyka")
artykul2.dodaj_tag("technologia")
artykul2.dodaj_tag("uczenie_maszynowe")
artykul2.dodaj_tag("medycyna")

session.commit()