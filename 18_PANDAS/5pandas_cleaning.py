import pandas as pd

df = pd.read_csv('data3.csv')

print(df)

# DROPNA, FILLNA

new_df = df.dropna()    # dropna - usuwa puste wiersze, nie zmienia starej tabeli tylko tworzy nowa
print(new_df)

# df.dropna(inplace = True)     # inplace = True zmienia stara tabele
# print(df)                     # nie wlaczam tego bo nie chce zmieniac starej tabeli

new_df2 = df.fillna(130)    # zamienia puste komorki na zadana wartosc
                            # tutaj tez mozna dodac "inplace = Truth"

print(new_df2)

print(df.columns.tolist())  # wyswietla naglowki kolumn

new_df3 = df.fillna({"Calories": 130})   # zamienia tylko puste wiersze w kolumnie "Calories"

print(new_df3)

# MEAN, MEDIAN, MODE

x = df["Calories"].mean()   # x staje sie srednia wartoscia z kolumny Calories

new_df4 = df.fillna({"Calories": x})

print(new_df4)

y = df["Calories"].median()     # y - mediana wartosci z kolumny

new_df5 = df.fillna({"Calories": y})

print(new_df5)

z = df["Calories"].mode()[0]    # mode - wartosc ktora jest wyswietlana najczesciej

new_df6 = df.fillna({"Calories": z})

print(new_df6)