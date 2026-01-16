import pandas as pd

df = pd.read_csv('data3.csv')

print(df)

new_df = df.dropna()    # dropna - usuwa puste wiersze, nie zmienia starej tabeli tylko tworzy nowa
print(new_df)

# df.dropna(inplace = True)     # inplace = True zmienia stara tabele
# print(df)                     # nie wlaczam tego bo nie chce zmieniac starej tabeli



