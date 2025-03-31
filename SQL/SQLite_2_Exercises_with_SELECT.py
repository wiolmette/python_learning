import sqlite3
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

# Ex. 1
cursor.execute("SELECT FirstName, LastName FROM customers;")
results = cursor.fetchall()
for row in results:
    print(row)

# Ex. 2
cursor.execute("SELECT * FROM tracks WHERE UnitPrice>0.99;")
results1 = cursor.fetchall()
for row in results1:
    print(row)

# Ex. 3
cursor.execute("SELECT Title FROM albums;")
results2 = cursor.fetchall()
for row in results2:
    print(row)

# Ex. 4
cursor.execute("SELECT * FROM employees WHERE ReportsTo>0;")
results4 = cursor.fetchall()
for row in results4:
    print(row)

# Ex. 5
cursor.execute("SELECT * FROM tracks ORDER BY Name ASC LIMIT 10;") # najpierw order, potem limit!
results5 = cursor.fetchall()
for row in results5:
    print(row)

cursor.close()
conn.close()