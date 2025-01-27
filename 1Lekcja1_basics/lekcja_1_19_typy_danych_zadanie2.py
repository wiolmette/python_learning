import statistics
liczba1 = int(input("Wprowadź pierwszą liczbę "))
liczba2 = int(input("Wprowadź drugą liczbę "))
liczba3 = int(input("Wprowadź trzecią liczbę "))
lista = [liczba1, liczba2, liczba3]
suma = liczba1 + liczba2 + liczba3
srednia = statistics.mean(lista)
minimum = min(lista)
maximum = max(lista)
print(suma, srednia, minimum, maximum)