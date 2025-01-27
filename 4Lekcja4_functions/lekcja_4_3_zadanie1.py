# Zadania z funkcji

# Zad. 1 Napisz funkcję silnia(), która oblicza silnię z podanej liczby. 
# Użyj pętli lub rekurencji, aby obliczyć wynik. 
# Silnia z liczby n to iloczyn wszystkich liczb od 1 do n.
# Rekurencja - funkcja ktora wywoluje sama siebie 

# Petla z printem
def silnia(n):
    wynik = 1
    for i in range(1, n+1):
        wynik = wynik*i
    print("Silnia z", n, "to", wynik)
silnia(6)

# Petla z return - zamiast wywoływać funkcję na koncu osobno, 
# wywołuję ją w princie
def silnia2(m):
    wynik2 = 1
    for j in range(1, m+1):
        wynik2 = wynik2*j
    return wynik2
print("Silnia2 to", silnia2(5))

# Rekurencja
def silnia3(o):