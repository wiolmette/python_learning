import sqlite3
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

# Zadanie typu 10 z lekcji 7, czyli gdy chcę użyć funkcji agregujących i jednocześnie wyświetlić 
# konkretny wiersz (np. nazwę), a grupuję po czymś innym (np. gatunku)

# Dla każdego kraju (BillingCountry) pokaż numer faktury (InvoiceId) o najniższej wartości (Total).

cursor.execute("""SELECT invoices.BillingCountry, invoices.InvoiceId, invoices.Total
               FROM invoices
               JOIN(SELECT BillingCountry,
               MIN(Total) AS min
               FROM invoices
               GROUP BY BillingCountry)
               AS minima ON minima.BillingCountry = invoices.BillingCountry
               AND minima.min = invoices.Total
               """)
results1 = cursor.fetchall()
print(results1)


# Zadania dodatkowe - dalsza nauka:

# 1. Wyświetl tytuły utworów z albumów artysty o nazwie „AC/DC”.

cursor.execute("""SELECT tracks.Name, albums.Title
               FROM tracks
               JOIN albums ON albums.AlbumId = tracks.AlbumId
               JOIN artists ON albums.ArtistId = artists.ArtistId
               WHERE artists.ArtistId = 1
               """)
results2 = cursor.fetchall()
print(results2)
