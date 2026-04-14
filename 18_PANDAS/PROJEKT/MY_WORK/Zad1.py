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
print(customers.isna().sum())         # liczba brakujacych wartosci
print("\nduplicated:")
print(customers.duplicated().sum())   # liczba duplikatow

print("\nDANE CUSTOMERS:\nliczba kolumn = ",customers.shape[0],"\nliczba wierszy = ",customers.shape[1],"\ntypy danych: object, int64\nbrak brakujacych wartosci\nbrak duplikatow\nprzykladowe rekordy wyswietlone ponizej\n")
print(customers.sample(5))                               # przykladowe rekordy

# orders:

print("\nORDERS:\n")
print("info:")
orders.info()         # liczba wierszy i kolumn, typy danych
print("\nisna:")
print(orders.isna().sum())         # liczba brakujacych wartosci
print("\nduplicated:")
print(orders.duplicated().sum())   # liczba duplikatow

print("\nDANE ORDERS:\nliczba kolumn = ",orders.shape[0],"\nliczba wierszy = ",orders.shape[1],"\ntypy danych: object, int64\nbrakujace wartosci: order_approved_at - 160, order_delivered_carrier_date - 1783, order_delivered_customer_date - 2965\nbrak duplikatow\nprzykladowe rekordy wyswietlone ponizej\n")

print(orders.sample(5))    


# 4. Narysuj prostą mapę relacji między tabelami:
# - która tabela jest główna,
# - po jakich kluczach da się łączyć dane.

# Relacja: customers (1) → orders (N)
# Klucz łączenia: customer_id
# Opis: jeden klient może mieć wiele zamówień
# Ktora tabela glowna: Tabela centralna: orders
# Uzasadnienie:
# orders jest tabelą faktów i zawiera zdarzenia biznesowe (zamówienia),
# dlatego stanowi główną tabelę w analizie.
# Dodatkowo:
# customers jest tabelą nadrzędną w modelu danych (relacja 1 → N),
# ponieważ jeden klient może mieć wiele zamówień.

# 5. Zapisz 5 pierwszych obserwacji o jakości danych.

# I W tabeli customers nie ma brakujacych wartosci.
# II W tabeli customers nie ma duplikatow.
# III W tabeli orders 3 kolumny zawieraja brakujacych wartosci.
# IV W tabeli orders nie ma duplikatow.
# V 