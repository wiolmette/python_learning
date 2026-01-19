import pandas as pd

df = pd.read_csv('data3.csv')

# Zmiana danych w zlym formacie

print(df)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')   # zmienia date na odpowiedni format

# we wierszu 26 jest 2020/12/26, a powinno byc '2020/12/26' --> zmienilo
# we wierszu 22 jest pusta komorka, wiec zmienilo NaN na NaT (Not a Time) 

print(df)

df2 = df.dropna(subset=['Date'])    # usuwa puste komorki w kolumnie "Date"

print(df2)

# Zamiana danych (gdy zauwazymy ze dane sa bledne i chcemy zamienic na wlasciwe)

df.loc[7, 'Duration'] = 405        # zamienia 7-my wiersz kolumny Duration na 405

print(df)

for x in df.index:                      # df.index - obiekt przechowujacy etykiety wierszy
                                        # for x in df.index - iterowanie po wszystkich indeksach
 if df.loc[x, "Duration"] > 120:        # jesli wartosc we weirszu "Duration" jest wieksza niz 120
    df.loc[x, "Duration"] = 121         # to zamien ja na 120

print(df)

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)          # usuwa wiersz z Duration > 120

print(df)

# DUPLICATES

print(df.duplicated())        # wypisuje wiersze z info czy jest duplikatem

df.drop_duplicates(inplace = True)      # usuwa wiersze bedace duplikatami

print(df)