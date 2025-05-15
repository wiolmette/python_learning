import sqlite3
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()

# Zadania z GROUP BY, COUNT, SUM, AVG, MAX, MIN, ORDER BY, LIMIT

# 1. Policz, ilu klientów pochodzi z każdego miasta. Posortuj miasta od największej do najmniejszej liczby klientów.
cursor.execute("""SELECT City, COUNT (*) AS liczba_klientow
               FROM customers
               GROUP BY City
               ORDER By liczba_klientow ASC""")
results1 = cursor.fetchall()
print(results1)

# 2. Oblicz łączną wartość faktur (Total) wystawionych w każdym kraju. Pokaż tylko te kraje, gdzie suma przekracza 50.
cursor.execute("""SELECT BillingCountry, SUM(Total)
               FROM invoices
               GROUP BY BillingCountry
               ORDER BY Total ASC
               LIMIT 50""")
results2 = cursor.fetchall()
print(results2)

# 3. Pokaż średnią długość utworu (w sekundach) dla każdego gatunku.
cursor.execute("""SELECT genres.Name, AVG(Milliseconds)
               FROM tracks
               JOIN genres 
               ON genres.GenreId = tracks.GenreId
               GROUP BY genres.Name""")
results3 = cursor.fetchall()
print(results3)

# 4. Dla każdego typu nośnika (MediaType), policz, ile utworów jest z nim powiązanych i podaj ich łączną długość.
cursor.execute("""SELECT media_types.Name, COUNT(*), SUM(Milliseconds)
               FROM tracks
               JOIN media_types
               ON tracks.MediaTypeId = media_types.MediaTypeId
               GROUP BY media_types.Name""")
results4 = cursor.fetchall()
print(results4)

# 5. Pokaż 5 gatunków z najkrótszą łączną długością utworów (czyli SUM(Milliseconds)).
cursor.execute("""SELECT genres.Name, SUM(Milliseconds) AS laczna_dlugosc
               FROM tracks
               JOIN genres ON genres.GenreId = tracks.GenreId
               GROUP BY genres.Name
               ORDER BY laczna_dlugosc ASC
               LIMIT 5""")
results5 = cursor.fetchall()
print(results5)

# 6. Wyświetl artystów, którzy mają więcej niż 3 albumy.
cursor.execute("""SELECT artists.Name, COUNT(*) AS liczba_albumow
               FROM albums
               JOIN artists ON albums.ArtistId = artists.ArtistId
               GROUP BY albums.ArtistId
               HAVING COUNT(*) > 3
               ORDER BY liczba_albumow ASC""")
results6 = cursor.fetchall()
print(results6)

# 7. Policz, ile utworów jest powiązanych z każdą playlistą i posortuj wyniki malejąco.
cursor.execute("""SELECT playlists.Name, COUNT(*) AS liczba_utworow
               FROM playlist_track
               JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
               GROUP BY playlist_track.PlaylistId
               ORDER BY liczba_utworow DESC""")
results7 = cursor.fetchall()
print(results7)

# 8. Dla każdego klienta policz, ile faktur wystawiono i jaka była ich łączna wartość. Pokaż tylko klientów z co najmniej 2 fakturami.

# 9. Dla każdego kraju policz średnią wartość jednej faktury (AVG(Total)). Posortuj od najwyższej.

# 10. Pokaż najdłuższy utwór w każdym gatunku (czyli MAX(Milliseconds) pogrupowane po Genre).