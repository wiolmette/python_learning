a = int(input("Wprowadz a "))
b = int(input("Wprowadz b "))
c = a+b
d = a*b
e = a-b
f = a/b
dzialanie = int(input("wprowadz typ dzialania: 1 - suma, 2 - iloczyn, 3 - roznica, 4 - iloraz "))
if dzialanie == 1:
    print(f"Wynik dodawania to {c}")
if dzialanie == 2:
    print(f"Wynik mnozenia to {d}")
if dzialanie == 3:
    print(f"Wynik odejmowania to {e}")
if dzialanie == 4:
    print(f"Wynik dzielenia to {f}")