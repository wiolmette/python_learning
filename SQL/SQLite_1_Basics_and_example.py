import sqlite3

# trzeba byc w folderze SQL (File -> open folder ...) !!!
# >sqlite: open database ... (otwieram wybrana baze danych)

conn = sqlite3.connect('baza.db')    # conn - connection, lacze sie z baza chinook

cursor = conn.cursor()  # tworze kursora

cursor.execute("SELECT * FROM albums;") 
# cursor.execute - utworzenie polecenia
# SELECT - query = kwerenda (SELECT lub JOIN) - wybieram dane z bazy, nad ktorym chce pracowac

results = cursor.fetchall()  # (pobieram te dane, ktore wczesniej wybralam; fetchone - wybiera 1 a nie wszystkie)
# results - tablica w pythonie

# nie printowac calej tabeli, lepiej np. for row in results, print row
for row in results:
    print(row)

cursor.close()
conn.close()
