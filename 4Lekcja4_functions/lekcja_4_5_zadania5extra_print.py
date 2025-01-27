# Zad. 5 extra Napisz funkcje który informuje o tym 
# czy podana liczba jest liczbą pierwszą. Do wykonania tego 
# zadania potrzebujesz pętli i wykorzysania flow control (if/else/itd).

liczba = int(input("Podaj liczbe do sprawdzenia czy jest pierwsza "))
def czy_pierwsza(liczba):
    for i in range (1, liczba+1):
        if liczba % i == 0 and i < liczba and i != 1:
            print("F")
            break
        elif liczba % i == 0 and i == liczba:
            print("T")
    i = i + 1
czy_pierwsza(liczba)
