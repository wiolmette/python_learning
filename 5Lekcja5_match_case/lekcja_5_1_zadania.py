# Zad. 1 Napisz program, który dopasowuje liczbę do kilku przypadków:
# Liczba jest mniejsza niż 10.
# Liczba jest większa niż 10, ale mniejsza niż 20.
# Liczba jest większa lub równa 20.

liczba = int(input("Wprowadz liczbe "))
match liczba:
    case _ if liczba < 10:
        print("Liczba jest mniejsza od 10")
    case _ if liczba > 10 and liczba < 20:
        print("Liczba jest większa niż 10, ale mniejsza niż 20")
    case _ if liczba >= 20:
        print("Liczba jest większa lub równa 20")