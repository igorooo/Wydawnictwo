from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

"""
    Plik na wszystkie inserty do bazy
"""


user2 = Kontrybutor('Jan Nowak', 'JNow', 'asdzxc', 'JN123@email.com')
session.add(user2)
session.commit()

artykul5 = Artykul('Zastosowanie penicyliny na frontach II Wojny Światowej', date(2010, 4, 1), 'Darmowy', user2)
artykul6 = Artykul('Najlepsze gleby do roślin strączkowych', date(2012, 7, 6), 'Platny', user2)
artykul7 = Artykul('Bytowanie naturalne Grubowarga Dwubarwnego', date(2012, 3, 4), 'Darmowy', user2)
session.add_all([artykul5, artykul7, artykul6])
session.commit()

artykul5.dodaj_tag("medycyna")
artykul5.dodaj_tag("historia")
artykul5.dodaj_tag("antybiotyki")
artykul5.dodaj_tag("penicylina")

artykul6.dodaj_tag("ekonomia")
artykul6.dodaj_tag("rolnictwo")
artykul6.dodaj_tag("geologia")
artykul6.dodaj_tag("fasola")

artykul7.dodaj_tag("akwarystyka")
artykul7.dodaj_tag("zoologia")
artykul7.dodaj_tag("grubowarg")
artykul7.dodaj_tag("pielęgnicowate")



user3 = Kontrybutor('Arkadiusz Abacki', 'abecadlo', 'abcdefg123', 'abacki@email.com')
session.add(user3)
session.commit()

artykula = Artykul('Efekt cieplarniany a dziura ozonowa', date(2018, 2, 1), 'Darmowy', user3)
artykulb = Artykul('Budowa wewnętrzna serca', date(2017, 4, 4), 'Platny', user3)
artykulc = Artykul('Samotność wśród studentów informatyki', date(2011, 3, 3), 'Darmowy', user3)
session.add_all([artykula, artykulb, artykulc])
session.commit()

artykula.dodaj_tag("efekt cieplarniany")
artykula.dodaj_tag("klimat")
artykula.dodaj_tag("ozon")

artykulb.dodaj_tag("mięśnie")
artykulb.dodaj_tag("serce")
artykulb.dodaj_tag("kardiologia")
artykulb.dodaj_tag("medycyna")

artykulc.dodaj_tag("informatyka")
artykulc.dodaj_tag("technologia")
artykulc.dodaj_tag("socjologia")
artykulc.dodaj_tag("relacje")


user4 = Kontrybutor('Adam Czwarty', 'czwarty', 'Czwarty4', 'Adam.Czwarty@email.com')
session.add(user4)
session.commit()

artykulq = Artykul('Muzyka skrzypcowa na dworach świata', date(2010, 2, 1), 'Darmowy', user4)
artykulw = Artykul('Muzyka klasyczna na dworach świata', date(2012, 3, 6), 'Platny', user4)
artykule = Artykul('Sieci pająków skakunów', date(2012, 3, 6), 'Darmowy', user4)
artykulr = Artykul('Technologiczne wykorzystanie Zyzusia Tłuściocha', date(2012, 3, 6), 'Darmowy', user4)
session.add_all([artykulq, artykulw, artykule])
session.commit()

artykulq.dodaj_tag("muzyka")
artykulq.dodaj_tag("historia")
artykulq.dodaj_tag("skrzypce")

artykulw.dodaj_tag("muzyka")
artykulw.dodaj_tag("historia")
artykulw.dodaj_tag("fortepian")
artykulw.dodaj_tag("Bach")

artykule.dodaj_tag("przemysł")
artykule.dodaj_tag("zoologia")
artykule.dodaj_tag("technologia")
artykule.dodaj_tag("pająki")

session.commit()

