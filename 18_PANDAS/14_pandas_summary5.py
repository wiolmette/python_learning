import pandas as pd

import matplotlib.pyplot as plt 

# Dla DataFrame z kilkoma kolumnami liczbowymi:
# oblicz macierz korelacji
# sprawdź, które dwie kolumny są najsilniej skorelowane

data = pd.read_csv('data4.csv')

print(data)

print(data.corr())

# najsilniejsza korelacja: Duration i Calories

corr = data.corr()

print(corr.abs().unstack().sort_values(ascending=False))        
# automatycznie uklada kolumny w porzadku od najsilniej skorelowanych do najmniej

# Zadanie 15
# Narysuj: wykres liniowy jednej kolumny
# wykres słupkowy dla drugiej
# histogram dla danych liczbowych

data.plot(kind = 'line', x = 'Duration', y = 'Calories')

plt.show()

data.plot(kind = 'bar', x = 'Pulse', y = 'Calories')

plt.show()

data.plot(kind = 'hist', x = 'Pulse', y = 'Maxpulse')

plt.show()

