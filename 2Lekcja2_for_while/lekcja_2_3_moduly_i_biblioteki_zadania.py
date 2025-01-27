# moduły i biblioteki (moduł to mniejsza biblioteka xd)
# moduł zawieraja funkcje
# mozna instalowac a nastepnie importowac do programu
# cale moduly, a mozna konkretne funkcje z nich
# przyklad modulu: random

# zadanie: Napisz program, który wylosuje 6 unikalnych liczb 
# z przedziału od 1 do 50, aby zasymulować losowanie Lotto.
# Podpowiedź: Możesz użyć funkcji random.sample(), 
# która zwraca listę unikalnych losowych elementów 
# z podanego zakresu.

import random
# SKLADNIA random.sample
# random.sample(population, k)
# population: sekwencja (lista, krotka, zbiór, itp.), z której chcesz pobrać losową próbkę.
# k: liczba elementów, które chcesz wybrać z populacji.
lista = [1, 2, 3, 4, 5]
x = random.sample(lista, 3)
print(x)
lista2 = list(range(1, 51))      # lista skladajaca sie z liczb od 1 do 50!!!
print(lista2)
y = random.sample(lista2, 6)
print("Generator lotto: ", y)
z = random.sample(range(1,51), 6)    # population to moze byc przedzial liczb!!!
print("Generator lotto2: ", z)