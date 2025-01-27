# Zad. 4 Zabawa (zadanie z gwiazdką)
# Stwórz funkcję zabawa_z_listami
# Funkcja ma:
# Przyjmować parametr param
# Stworzyć listę z 7 losowymi liczbami, wyprintować
# Dodać param na koniec i w środek listy (nie jako wartość ale jako element listy)
# Usunąć pierwszą liczbę z listy.
# Posortować listę w odwrotnej kolejności.

import random

#liczby = []
#for liczba in liczby:
    #liczby.append(random.randint)
#print(liczby)

param = input("Wprowadz param ")
def zabawa_z_listami(param): 
    liczby = [random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000), random.randint(1,1000)]
    liczby.append(param)                    # bez indexu append dodaje na koniec listy!!!
    index_srodek = len(liczby) // 2         # srodek listy!
    liczby.insert(index_srodek, param)      # z indexem insert!
    liczby.pop(0)                           # z indexem pop, bez remove!
    print(liczby)
    liczby.reverse()
    print(liczby)


zabawa_z_listami(param)
