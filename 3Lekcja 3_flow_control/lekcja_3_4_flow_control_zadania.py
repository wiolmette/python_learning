# Zad. 1 Sprawdź, czy liczba jest dodatnia, ujemna lub zerem
liczba = int(input("Wprowadz liczbe "))
if liczba > 0:
    print("Twoja liczba jest dodatnia")
elif liczba == 0:
    print("Twoja liczba jest zerem")
else:
    print("Twoja liczba jest ujemna")

# Zad. 2 Sprawdź, czy liczba jest podzielna przez 3 i 5
liczba2 = int(input("Wprowadz liczbe2 "))
if liczba2 % 3 == 0 and liczba2 % 5 ==0:
    print("Twoja liczba2 jest podzielna przez 3 i 5")
else:
    print("Twoja liczba2 nie jest podzielna przez 3 i 5")

# Sprawdze czy liczba jest podzielna przez 3, i jesli tak to czy tez przez 5
liczba3 = int(input("Wprowadz liczbe3 "))
if liczba3 % 3 == 0:
    print("Twoja liczba3 jest podzielna przez 3")
    if liczba3 % 5 == 0:
        print("Twoja liczba3 jest tez podzielna przez 5")
    else:
        print("Ale niestety nie jest podzielna przez 5")
else: 
    print("Twoja liczba3 nie jest podzielna przez 3")

# Sprawdze czy liczba jest podzielna przez 3 lub 5
liczba4 = int(input("Wprowadz liczbe4 "))
if liczba4 % 3 == 0 or liczba4 % 5 == 0:
    print("Twoja liczba4 jest podzielna przez 3 lub 5")
else:
    print("Twoja liczba4 nie jest podzielna przez 3 lub 5")