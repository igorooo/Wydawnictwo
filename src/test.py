from engine import *
from datetime import date
from uzytkownicy import *
from objects import *
from artykul import *

grupa = Grupa('Ortografia')
session.add(grupa)
session.commit()

user2 = Recenzent('Jan Nowak', 'JNow', 'asdzxc', 'JN123@email.com')
user3 = Recenzent('Tomasz Karolak', 'tomekkarolek', 'asdzxc', 'karol@email.com')
user4 = Recenzent('Szymon Tomczak', 'STom', 'asdzxc', 'stom@email.com')

session.add_all([user2, user3, user4])
session.commit()

grupa.weryfikanci.append(user2)
grupa.weryfikanci.append(user3)
grupa.weryfikanci.append(user4)

session.commit()
