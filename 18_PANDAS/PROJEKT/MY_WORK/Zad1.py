import pandas as pd

# 1. Pobierz dataset i umieść pliki CSV w data/.


# 2. Otwórz 2-4 najważniejsze pliki w pandas.


customers = pd.read_csv("E:/programowanie_git/python_learning/18_PANDAS/PROJEKT/data/olist_customers_dataset.csv")
orders = pd.read_csv("E:/programowanie_git/python_learning/18_PANDAS/PROJEKT/data/olist_orders_dataset.csv")
print("\nSTART")

# 3. Dla każdego pliku sprawdź:
# liczbę wierszy i kolumn,
# typy danych,
# brakujące wartości,
# duplikaty,
# przykładowe rekordy.

# customers:

print("\nCUSTOMERS:\n")
print("info:")
customers.info()         # liczba wierszy i kolumn, typy danych
print("\nisna:")
print(customers.isna())         # brakujace wartosci
print("\nduplicated:")
print(customers.duplicated())   # duplikaty

print("\nDANE CUSTOMERS:\nliczba kolumn = 5\nliczba wierszy = 99441\ntypy danych: object, int64\nbrak brakujacych wartosci\nbrak duplikatow\nprzykladowe rekordy wyswietlone ponizej\n")

print(customers)                               # przykladowe rekordy

# orders:

print("\nORDERS:\n")
print("info:")
orders.info()         # liczba wierszy i kolumn, typy danych
print("\nisna:")
print(orders.isna())         # brakujace wartosci
print("\nduplicated:")
print(orders.duplicated())   # duplikaty

print("\nDANE ORDERS:\nliczba kolumn = 5\nliczba wierszy = 99441\ntypy danych: object, int64\nbrak brakujacych wartosci\nbrak duplikatow\nprzykladowe rekordy wyswietlone ponizej\n")

print(orders)    


# 4. Narysuj prostą mapę relacji między tabelami:
# - która tabela jest główna,
# - po jakich kluczach da się łączyć dane.

# order dataset ---> order id ---> customer dataset
# order - glowna, customer - poboczna

# 5. Zapisz 5 pierwszych obserwacji o jakości danych.

# I Jakosc danych jest bardzo dobra.
# II Nie ma brakujacych wartosci.
# III Nie ma duplikatow.
# 