# Zad. 2 Napisz funkcję pomnoz(), która przyjmuje dwa argumenty liczbowe 
# i zwraca ich iloczyn. 
# Następnie wywołaj tę funkcję dla dowolnych wartości i wyświetl wynik.

def iloczyn(a,b):
    return a*b
wynik = iloczyn(4,8)
print(wynik)

# Zad. 3 Napisz funkcję czy_parzysta(), która przyjmuje liczbę jako argument 
# i zwraca informację, czy jest ona liczbą parzystą czy nieparzystą. 
# Wynik powinien być typu True lub False.

liczba = int(input("Podaj liczbe do sprawdzenia czy jest parzysta "))
def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False
print(czy_parzysta(liczba))

# Zad. 4 Napisz kalkulator który wykorzystuje funkcje 
# z zadania 2 i 3 oraz wykonuje inne działania matematyczne 
# (zaskocz mnie jakie). Wykorzystaj zagnieżdżenie funkcji.

def potegowanie(podstawa,potega):
    return podstawa**potega

a = int(input("Podaj a "))
b = int(input("Podaj b "))
podstawa = int(input("Podaj liczbe do potegowania (podstawe) "))
potega = int(input("Podaj potege "))
def kalkulator(a,b,liczba,podstawa,potega):
    iloczyn(a,b)
    print("Wynik mnozenia to ", iloczyn(a,b))
    czy_parzysta(liczba)
    print("Czy", liczba, "jest parzysta:", czy_parzysta(liczba))
    potegowanie(podstawa, potega)
    print(podstawa, "do potegi", potega, "to", potegowanie(podstawa, potega))
kalkulator(a,b,liczba,podstawa,potega)