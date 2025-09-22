import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[0])        # loc - do zwracania specyficznego wiersza, tutaj wiersza nr 0 (1szego), czyli Series

print(df.loc[[0, 1]])   # teraz wynik jest Data Frame

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])       # argument 'index' pozwala nadawac nazwy indeksow

print(df) 

print(df.loc["day2"])   # mozna odwolywac sie do konkretnych wierszy poprzez nazwe argumentu

df2 = pd.read_csv('data.csv')    # 'read_csv' to komenda odczytywania csv! read_json do json'ow itp.

print(df2)               

print(df2.head(2))       #     wyswietlanie naglowkow i pierwszych 2 wierszy DataFrame'u

print(df2.head())

print(df.head())
