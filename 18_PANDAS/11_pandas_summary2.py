import pandas as pd

# DATA FRAME

# 3. Utwórz DataFrame z danymi: imię, wiek, miasto. Dodaj minimum 5 wierszy.
# Następnie: wyświetl tylko kolumny imię i wiek, wyświetl tylko osoby powyżej 30 lat

ludzie = {"imie": ["Ania", "Basia", "Kasia", "Marek", "Kamil"],
          "wiek": [6, 35, 20, 36, 13],
          "miasto":["Gdanks", "Wroclaw", "Warszawa", "Szczecin", "Sosnowiec"]}

df = pd.DataFrame(ludzie)

print(df)

print(df[["imie"]])

print(df[["imie", "wiek"]])

powyzej30 = df[df["wiek"] > 30]

print(powyzej30)

powyzej30_2 = df[df["wiek"] > 30][["imie", "wiek"]] 

print(powyzej30_2)

# 4 Dodaj nowa kolumne pelnoletni (True/False) na podstawie wieku

df["pelnoletni"] = df["wiek"] >= 18

print(df)