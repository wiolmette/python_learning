import pandas as pd

# ZADANIA OD CHATA

# I SERIES

# 1. Utwórz Series z nazwami 5 owoców i przypisz im indeksy będące liczbami od a do e.
# Wyświetl:
# cały obiekt
# element o indeksie 3 oraz o nazwie indeksu "b" 
# dwa pierwsze elementy

owoce = ["jablko", "banan", "mandarynka", "winogrono", "gruszka"]

series = pd.Series(owoce)

print(series)  

print(series[3])

print(series.iloc[0:2])        # komenda do pobierania wiecej niz 1 elementu series (tutaj 21 i 2 element)!!!
                               # iloc - po indeksach!!! (loc - po nazwach)

series2 = pd.Series(owoce, index = ["a", "b", "c", "d", "e"])

print(series2)

print(series2["b"])     # gdy zmieni sie indeksy z liczb na litery, to trzeba sie juz do liter odwolywac!!!

print(series2.loc["a":"c"])     # pobiera elemeny o nazwach indeksach od a do c

# 2. Utwórz Series z temperaturami tygodnia (7 wartości). Sprawdź: średnią, maksimum, minimum

temperatury = [1, 3, -5, 10, 20, 43, -18]

series3 = pd.Series(temperatury)

series3 = pd.Series(temperatury, index = ["poniedzialek", "wtorek", "sroda", "czwarek", "piatek", "sobota", "niedziela"])

print(series3)

x = series3.mean()

print(x)

y = series3.max()

print(y)

z = series3.min()

print(z)