1.  Postawić lokalnie bazę mariadb:
    'mysql+pymysql://root@localhost:3306/OWydawnictwo'
    mysql+pymysql - dialekt
    root - uzytkownik (jeśli mamy hasło dla uzytkownika to: root:haslo@localhost:...)
    3306 - port
    OWydawnictwo - nazwa bazy
2.  sudo pip3 install sqlalchemy
3.  prawdopodobnie wymagane do python2 (pominąć ten krok, wrócić jeśli nie będzie działało)
    apt-get install python-mysqldb //ubuntu
    Na Archu prawdopodobnie:
    sudo pacman -S mysql-python
    jeśli nie to sprawdzić tu:
    https://stackoverflow.com/questions/454854/no-module-named-mysqldb (post sprzed 11 lat, python2)
4. sudo pip3 install PyMySQL
