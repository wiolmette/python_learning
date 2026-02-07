import pandas as pd

# 8. Dla dowolnego DataFrame:
# policz średnią jednej kolumny liczbowej
# sprawdź ile jest unikalnych wartości w innej kolumnie (nunique())

df = pd.read_csv("data4.csv")

print(df[["Calories"]].mean())

print(df[["Duration"]].nunique())   # - liczy ile jest unikalnych wartosci danych, tzn. ile roznych wartosci wystepuje

# 9. Posortuj dane: rosnąco po jednej kolumnie, malejąco po innej

print(df.columns)

print(df.sort_values("Pulse"))

print(df.sort_values("Maxpulse", ascending = False))

# 10. Utwórz DataFrame z brakującymi wartościami (NaN).
# uzupełnij braki średnią kolumny 
# Następnie: usuń wiersze z brakami

ludzie = {"imie": ["Wiola", "Konrad", "Aga","Ola"],
          "nazwisko":[None,"Nowak","Arab", "Dzik"],
          "wiek": [1, 121, None, 20]}

ludzie2 = pd.DataFrame(ludzie)

print(ludzie2)

x = ludzie2["wiek"].mean()

ludzie3 = ludzie2.fillna({"wiek": x})

print(ludzie3)

ludzie3.dropna(inplace = True)

print(ludzie3)


# 11. Utwórz kolumnę z datami zapisanymi jako string. Zamień ją na typ datetime i sprawdź dtypes.

ludzie3["data urodzenia"] = ["01.02.1998", "05.08.1980", "07.12.2001"] 

print(ludzie3)

ludzie3['data urodzenia'] = pd.to_datetime(ludzie3['data urodzenia'], format='mixed')

print(ludzie3)

print(ludzie3.dtypes)

# 12. W kolumnie wiek ustaw maksymalną wartość na 120. Jeśli ktoś ma więcej, zamień na 120.

# nie uzyway IF na calych kolumnach!!!

# df.loc[x, 'Nazwa_kolumny'] = y 

ludzie3.loc[ludzie3["wiek"] > 120, 'wiek'] = 120

print(ludzie3)

# 13. Dodaj do DataFrame duplikujące się wiersze.
# Sprawdź: mile jest duplikatów, usuń je, porównaj liczbę wierszy przed i po