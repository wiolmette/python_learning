import pandas as pd

df = pd.read_csv('data3.csv')

# df.corr()       # liczy korelacje miedzy wartosciami w kolumnach, wszystkie komorki musza miec wartosci numeryczne!
                  # dlatego najpierw zmienie tabele poznanymi sposobami aby zawierala same dane numeryczne

print(df)

# wiersz 7 Duration: 450 ---> zamienic na np mean
# wiersz 18 Calories NaN ---> median
# wiersz 22 Date NaN ---> usunac
# wiersz 26 Date zly format ---> ustawic dobry format
# wiersz 28 Calories Nan ---> median

x = df["Duration"].mean()
df.loc[7, 'Duration'] = x        # zamienia x-y wiersz zadanej kolumny na wartość y
print(df)

y = df["Calories"].median()  		
df = df.fillna({"Calories": y})	    # zamienia puste komórki na średnią wartość z kolumny
print(df)

df = df.dropna(subset=['Date'])     # usuwa wiersz z pusta komorka w kolumnie Date
print(df)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')     # zmienia format daty na prawidłowy
print(df)

print(df.corr())

# teoretycznie powinno byc: "Duration" and "Calories" got a 0.922721 correlation, 
# which is a very good correlation, and we can predict that the longer you work out, 
# the more calories you burn, 
# and the other way around: if you burned a lot of calories, you probably had a long work out.

