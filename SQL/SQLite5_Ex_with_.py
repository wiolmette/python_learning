import sqlite3
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()


# 15. Policz ilu klientów pochodzi z każdego kraju.
cursor.execute("""SELECT DISTINCT Country FROM customers;""")

results15 = cursor.fetchall()
for row in results15:
    print(row)

cursor.execute("SELECT CustomerId FROM customers WHERE Country='Brazil';")
results16 = cursor.fetchall()
for row in results16:
    print(row)

print(results16)
print(len(results16))
print("The number of customers from Brazil is", len(results16))

print(results15)
print(type(results15))
print(results15[0])
print(results15[len(results15)-1])

country1 = results15[0]
print(country1)
print(type(country1))
country2 = results15[0][0]
print(country2)
print(type(country2))

# WAŻNE!!! Nie mozna napiac Country=country2, bo country2 traktowane jest jak string
# Trzeba uzyc takiej skladni jak na dole ze znakiem zapytania i potem nawiasem itp.
cursor.execute("SELECT CustomerId FROM customers WHERE Country=?;", (country2,))
results18 = cursor.fetchall()
print(results18)

for i in range(0, len(results15)):
    country = results15[i][0]
    cursor.execute("SELECT CustomerId FROM customers WHERE Country=?;", (country,))
    results17 = cursor.fetchall()
    # print(results17)
    print("Number of clients from", country, "is", len(results17))


# 16. Policz ile utworów znajduje się w każdym gatunku (Genre).
cursor.execute("SELECT COUNT(tracks.GenreId) FROM tracks JOIN genres ON tracks.GenreId = genres.GenreId;")
results19 = cursor.fetchall()
print(results19)
for row in results19:
    print(row)



#print(type(results19))
#print(results19[0])




#     cursor.execute("SELECT CustomerId FROM customers WHERE Country=?;", (country,))
#     results17 = cursor.fetchall()
#     # print(results17)
#     print("Number of clients from", country, "is", len(results17))

# 17. Oblicz średnią cenę utworu.

# 18. Znajdź 3 gatunki z największą liczbą utworów.

# 19. Policz łączną długość (w sekundach) wszystkich utworów w bazie.