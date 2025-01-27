# Pętla while wykonuje blok kodu dopóki 
# warunek logiczny jest prawdziwy
# SKLADNIA
# while warunek:
    # blok kodu
i = 0               # trzeba zdefiniowac startowa wartosc 
while i < 5:       
    print(i)
    i += 1          # += 1 - zwieksz o 1, to samo co i = i+1

# Zadanie 2: Stwórz pętlę while, 
# która będzie wypisywać liczby parzyste mniejsze od 20.
j = 0
while j < 20:
    print(j)
    j += 2          # inaczej: j = j + 2

# Zadanie 3: Napisz pętlę, która przerwie swoje działanie, gdy 
# natrafi na liczbę podzielną przez 7 w zakresie od 1 do 100.
k = 1
while k < 100:
    if k/7 == 1:
        break
    print (k)
    k += 1

# sposob z modulo (%), czyli reszta dzielenia
# reszta = a % b
reszta = 10 % 7
print(reszta)
# jesli reszra z dzielenia = 0, to znaczy ze dana liczba
# jest podzielna przez dana liczbe
reszta2 = 10 % 10
print(reszta2)

l = 1
while l < 100:
    if l % 7 == 0:
        break
    print (l)
    l += 1