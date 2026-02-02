import pandas as pd
import matplotlib.pyplot as plt         # bilbioteka do wykresow

df = pd.read_csv('data3.csv')

df["Duration"] = df["Duration"].astype("float")     # zamienia kolumne Duration z liczb calkowitych na ulamkowa

x = df["Duration"].mean()
df.loc[7, 'Duration'] = x        # zamienia x-y wiersz zadanej kolumny na wartość y

y = df["Calories"].median()  		
df = df.fillna({"Calories": y})	    # zamienia puste komórki na średnią wartość z kolumny

df = df.dropna(subset=['Date'])     # usuwa wiersz z pusta komorka w kolumnie Date

df['Date'] = pd.to_datetime(df['Date'], format='mixed')     # zmienia format daty na prawidłowy

df = df.drop(columns=["Date"])          # usuniecie kolumny "Date"

print(df)

df.plot()

plt.show()