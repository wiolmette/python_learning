import pandas as pd         # pandas jako alios pd aby latwiej sie do niego pozniej odwolywac

# ---

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],             # przykladowa Series (cos jak kolumna danych)
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# ---

print("pandas version:", pd.__version__)    # sprawdzanie wersji pandas

# ---

a = [1, 7, 2]           # Series jako lista, wtedy indeksy automatyczne
myvar2 = pd.Series(a)
print(myvar2)

# ---

print(myvar2[0])        # wybor 1szej wartosci z Series


# ---

myvar3 = pd.Series(a, index = ["x", "y", "z"])      # indeksowanie danych inaczej niz auotmatycznie czyli 0, 1, 2, ...

print(myvar3)

# ---

print(myvar3["y"])          # odnoszenie sie do nadanego samemu indeksu

# ---

calories = {"day1": 420, "day2": 380, "day3": 390}      # Series mozna tez definiowac jako klucz-wartosc

myvar4 = pd.Series(calories)

print(myvar4)

# ---

myvar5 = pd.Series(calories, index = ["day1", "day2"])      # wybieranie tylko niektorych kluczy i wartosci

print(myvar5)

# ---

# Data frame - multi-dimensional table

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar6 = pd.DataFrame(data)

print(myvar6)

# Series - pojedyncza kolumna (1D)
# Data frame - tabela 2D (wiele wierszy i kolumn)