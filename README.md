1.  Zamiast MySQL użyłem SQLite, więc nie trzeba stawiać servera, cała baza jest w pliku Wydawnictwo.
    Polecam odpalić projekt w PyCharm Professional (Konto można aktywować studenckim mailem), podgląd bazy zapewnia Database plugin (prawy panel)
    W pluginie trzeba dodać ścieżkę do bazy.
    Jeśli z jakiegoś powodu nie lubisz się z pycharmem, to proponuję do podglądu bazy w sqlite:
    - https://github.com/pawelsalawa/sqlitestudio/releases
    
2.  Potrzebne moduły:  
-sqlalchemy
-może coś do sqlite
-pycharm sam pobierze po wyklikaniu serownik do sqlite, w innym przypadku na linuxie zainstalowac sqlite3

3. Nazwy backrefow, czasami atrybutow i relacji są pisane bez żadnej konwencji (potrzbny refactoring)
   W pliku main.py są przykładowe operacje dodawani obiektów (raczej wszystkie możliwe)
   Trzeba pamiętać o commitowaniu w odpowiednim momencie.

4. Polecam wstęp do SqlAlchemy:
   https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html?fbclid=IwAR1weHKGxRTC7C2qfN9lLWxZOTWMrQaBhK3xDjxG6t30I50cRbIQ0FMdIQc

