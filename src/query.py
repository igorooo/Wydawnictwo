from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

"""
    Plik na zapytania 
"""

"""
    Zapytanie o dostepnosc wszystkich artykulow
"""

query = session.query(Artykul).order_by(Artykul.id)

print('--- Dostępność Artykułów ---')
for a in query:
    print(a.id, a.nazwa, a.dostepnosc)

"""
    Zapytanie o artykuły posiadające podany tag
"""

query = session.query(Artykul, Tag).join(Artykul.tagi).filter(Tag.tag == 'technologia')

print('---------- Artykuły zawierające podany tag: ')
for c, t in query:
    print(c.nazwa)


"""
    Zapytanie o artykuły dodane przez użytkownika o imieniu Tomasz Kowalski i loginie 'kowalski'
"""
query = session.query(Artykul, Uzytkownik).join(Artykul.kontrybutor).filter(Uzytkownik.nazwa == 'Tomasz Kowalski')\
                                                                    .filter(Uzytkownik.login == 'kowalski')
print('-------- Artykuły podane przez podanego Użytkownika: ')
for c, t in query:
    print(c.nazwa)


"""
    Zapytanie o ilość darmowych artykułów w bazie
"""
query = session.query(Artykul).filter(Artykul.dostepnosc == 'Darmowy').count()


print('-------- Ilość darmowych artykułów w bazie: ', end='')
print(query)


"""
    Zapytanie o skład recenzentów w grupie weryfikacyjnej o id: 4
"""


q = session.query(Recenzent).join(weryfikanci_table).filter(weryfikanci_table.c.idGrupa == 4)

print("---------- Recenzencie wchodzący w skład grupy weryfikacyjnej o podanym id:")
for r in q:
    print(r.nazwa)





