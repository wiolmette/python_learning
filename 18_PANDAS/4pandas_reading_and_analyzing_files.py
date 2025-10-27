import pandas as pd

# CSV

df2 = pd.read_csv('data.csv')    # 'read_csv' to komenda odczytywania csv! read_json do json'ow itp.

print(df2)               

print(df2.head(2))       # wyswietlanie naglowkow i pierwszych 2 wierszy DataFrame'u

print(df2.head(5))        # wyswietlanie naglowkow i pierwszych 5 wierszy DataFrame'u

print(df2.head())

print(df2.to_string())   # ".to_string" powoduje, ze wyswietla sie caly plik a nie tylko pierwsze i ostatnie 5 kolumn


print(pd.options.display.max_rows)  # wyswietla maksymalna liczbe rzedow, czyli taka powyzej ktorej print 
                                    # bedzie wyswietlac 5 pierwszych i 5 ostatnich rzedow

pd.options.display.max_rows = 9999  # zmiana maksymalnej liczby wierszy 

# JSON

df3 = pd.read_json('data.json')

print(df3)

print(df2.tail(3))      # wyswietlanie naglowkow i 3 ostatnich wierszy

print(df2.info())

print(df3.to_string())      # printuje caly plik (calego data frame'a)

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df4 = pd.DataFrame(data)

print(df4)

