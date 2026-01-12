import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)

print("df.loc[0]: ", df.loc[0])        # loc - do zwracania specyficznego wiersza, tutaj wiersza nr 0 (1szego) (wynik to Series)

print("df.loc[[0, 2]]: ", df.loc[[0, 2]])   # odwolywanie sie do wierszy od 0 do 1 (teraz wynik jest Data Frame) 

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])       # argument 'index' pozwala nadawac nazwy indeksow

print(df) 

print(df.loc["day2"])   # mozna odwolywac sie do konkretnych wierszy poprzez nazwe argumentu
