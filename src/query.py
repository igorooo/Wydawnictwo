from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

"""
    Plik na zapytania 
"""

# Przykladowy JOIN
query = session.query(Artykul, Uzytkownik).filter(Artykul.kontrybutor_id == Uzytkownik.id).all()

for c, i in query:
    print(c.nazwa, i.nazwa)





