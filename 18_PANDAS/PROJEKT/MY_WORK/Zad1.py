import pandas as pd

# Pobierz dataset i umieść pliki CSV w data/.

# Otwórz 2-4 najważniejsze pliki w pandas.

df = pd.read_csv("E:/programowanie_git/python_learning/18_PANDAS/PROJEKT/data/olist_customers_dataset.csv")

# Dla każdego pliku sprawdź:
# liczbę wierszy i kolumn,
# typy danych,
# brakujące wartości,
# duplikaty,
# przykładowe rekordy.

print("info\n", df.info())              # liczba wierszy i kolumn, typy danych
print("isna:\n", df.isna())             # brakujace wartosci
print("duplicated:\n", df.duplicated())   # duplikaty

print("\nDANE:\nliczba kolumn = 5\nliczba wierszy = 99441\ntypy danych: object, int64\nbrak brakujacych wartosci\nbrak duplikatow\nprzykladowe rekordy wyswietlone ponizej")

print(df)                               # przykladowe rekordy