from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

"""
    Plik na zapytania 
"""

"""
    Zapytanie o artykuły posiadające podany tag
"""
query = session.query(Artykul, Tag).join(Artykul.tagi).filter(Tag.tag == 'technologia')

for c, t in query:
    print(c.nazwa)


"""
    Zapytanie o artykuły dodane przez użytkownika o imieniu Toamsz Kowalski i loginie 'kowalski'
"""
query = session.query(Artykul, Uzytkownik).join(Artykul.kontrybutor).filter(Uzytkownik.nazwa == 'Tomasz Kowalski')\
                                                                    .filter(Uzytkownik.login == 'kowalski')

for c, t in query:
    print(c.nazwa)










