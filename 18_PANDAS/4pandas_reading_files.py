import pandas as pd

# CSV

df2 = pd.read_csv('data.csv')    # 'read_csv' to komenda odczytywania csv! read_json do json'ow itp.

print(df2)               

print(df2.head(2))       # wyswietlanie naglowkow i pierwszych 2 wierszy DataFrame'u

print(df2.head())        # wyswietlanie naglowkow i pierwszych 5 wierszy DataFrame'u

print(df2.head())

# print(df2.to_string())   # ".to_string" powoduje, ze wyswietla sie caly plik a nie tylko pierwsze i ostatnie 5 kolumn


print(pd.options.display.max_rows)  # wyswietla maksymalna liczbe rzedow, czyli taka powyzej ktorej print 
                                    # bedzie wyswietlac 5 pierwszych i 5 ostatnich rzedow

pd.options.display.max_rows = 9999  # zmiana maksymalnej liczby wierszy 

# JSON

df3 = pd.read_json('data.json')

print(df3)


print(df2.tail())

print(df2.info())
