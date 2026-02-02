import pandas as pd

# 5. Wczytaj dowolny prosty plik CSV (może być z internetu albo własny). Sprawdź:
# head(), tail(), info(), describe()

data = pd.read_csv("data.csv")

print(data)

print(data.head())

print(data.tail())

print(data.info())

print(data.describe())

# 6. Z pliku CSV wybierz tylko 1 kolumne i zapisz je do nowego DataFrame.

data2 = data[["1440.699951172"]]

print(data2)

# 7. Wczytaj prosty plik JSON do DataFrame. 
# Wyświetl: listę kolumn, liczbę wierszy, pierwszy i ostatni rekord

data3 = pd.read_json('data.json')

print(data3)

print(data3.columns)

print(len(data3))

print(data3.head(1))
print(data3.tail(1))