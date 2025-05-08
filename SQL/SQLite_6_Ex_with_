import sqlite3
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()


# 20. Wstaw nowego klienta do tabeli customers.
cursor.execute("SELECT COUNT(CustomerId) FROM customers")
results25 = cursor.fetchall()
print(results25)
cursor.execute("""INSERT INTO customers (CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Email, SupportRepId)
               VALUES (60, 'Wioletta', 'Kopec', 'IMP', 'Fiszera 14', 'Gdansk', 'Pomorze', 'Polska', '80-504', '606196746', 'wiolmette@gmail.com', 5)""")

cursor.execute("SELECT * FROM customers WHERE CustomerId = 60")
result26 = cursor.fetchone()
print(result26)

# 21. Zaktualizuj numer telefonu klienta o CustomerId = 10.
cursor.execute("""UPDATE customers 
               SET Phone = 111222333
               WHERE CustomerId = 1""")

cursor.execute("SELECT Phone FROM customers WHERE CustomerId = 1")
result27 = cursor.fetchall()
print(result27)

cursor.execute("SELECT * FROM customers WHERE CustomerId = 1")
result28 = cursor.fetchall()
print(result28)

# 22. Zmień nazwę playlisty o PlaylistId = 5 na „Moje ulubione”
cursor.execute("""UPDATE playlists 
               SET Name = 'Moje ulubione'
               WHERE PlaylistId = 5""")

cursor.execute("SELECT * FROM playlists WHERE PlaylistId = 5")
result28 = cursor.fetchall()
print(result28)

# 23. Usuń pracownika, który ma EmployeeId = 8
cursor.execute("""DELETE FROM employees 
               WHERE EmployeeId = 8""")

cursor.execute("SELECT * FROM employees WHERE EmployeeId = 8")
result29 = cursor.fetchall()
print(result29)

# 24. Zmień cenę utworu TrackId = 3 na 0.89.
cursor.execute("""UPDATE tracks 
               SET UnitPrice = 0.89
               WHERE TrackId = 3""")

cursor.execute("SELECT * FROM tracks WHERE TrackId = 3")
result30 = cursor.fetchall()
print(result30)