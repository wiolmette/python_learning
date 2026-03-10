# II ZADANIA

import pandas as pd

df = pd.DataFrame({
    "miasto": ["Gdansk", "Gdansk", "Warszawa", "Warszawa", "Krakow"],
    "wiek": [25, 30, 22, 40, 35],
    "zarobki": [5000, 7000, 4500, 10000, 6500],
    "plec": ["K", "M", "K", "M", "K"]
})

# Zad. 1 Wyświetl tylko kolumnę wiek.

print(df["wiek"])

# Zad. 2 Policz średni wiek w całym DataFrame.

sredni_wiek = df["wiek"].mean()
print("sredni wiek to:", sredni_wiek)

# Zad. 3 Policz średni wiek dla każdego miasta.

sredni_wiek_w_miescie = df.groupby("miasto")["wiek"].mean()
print("sredni wiek w danych miastach to:", "\n", sredni_wiek_w_miescie)

# Zad. 4 Policz: sredni wiek i sume zarobków dla każdego miasta w jednej komendzie.

suma_i_srednia = df.groupby("miasto").agg({
    "wiek": "mean",
    "zarobki": "sum"
})
print(suma_i_srednia)

# Zad. 5 Wybierz osoby, które mają więcej niż 30 lat

print(df[df["wiek"] > 30])

# Zad. 6 Posortuj dane po zarobkach malejąco.

print(df.sort_values("zarobki", ascending=False))

# Zad. 7 Dodaj nową kolumnę: zarobki_roczne = zarobki * 12

df["zarobki_roczne"] =  df["zarobki"]*12
print(df)

# Zad. 8 Policz ile jest kobiet i mężczyzn.

kobiety = df[df["plec"] == "K"]
print(len(kobiety))

mezczyzni = df[df["plec"] == "M"]
print(len(mezczyzni))

# Zad. 9 Sprawdź czy są jakieś brakujące dane.

print(df.isna().sum())

# Zad. 10 Zresetuj indeks po sortowaniu.

df.reset_index
print(df)


# PYTANIA NA MYSLENIE ANALITYCZNE
# 1️⃣ Kiedy użyjesz groupby() zamiast filtrowania?
# 
 
# 2️⃣ Kiedy histogram jest lepszy niż wykres słupkowy? 
#

# 3️⃣ Dlaczego po groupby() kolumna po której grupujesz staje się indeksem? 
#

# 4️⃣ Co się stanie jeśli zrobisz: df.groupby("miasto").mean() a masz w DataFrame kolumny tekstowe?
#