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


# III PYTANIA NA MYSLENIE ANALITYCZNE

# 1️⃣ Kiedy użyjesz groupby() zamiast filtrowania?
# groupby uzyje kiedy chce przeanalizowac inna kolumne od tej,
# wzgledem ktorej grupuje i wyciagnac z niej jakies dane
# statystyczne
# filtrowanie uzyje, gdy z jednej kolumny chce znalezc
# wiersze, ktore spelaniaja jakis warunek
 
# 2️⃣ Kiedy histogram jest lepszy niż wykres słupkowy? 
# histogram jest lepszy, gdy chcemy zobaczyc jaki jest rozklad
# jednej zmiennej liczbowej, np. ile osob zarabia 5 tys zl, ile 10 itd.,
# a wykres slupkowy gdy mamy rozne zmienne i sprawdzay np.
# ile osob pali weglem drzewnym, a ile uzywa pomp ciepla

# 3️⃣ Dlaczego po groupby() kolumna po której grupujesz staje się indeksem? 
# Wiem, ze sie tak dzieje - czy to wazne dlaczego?
# Po groupby powstaje nowa tabela agregacji. Ta tabela ma:
# - jedną wartość dla każdej grupy
# - więc kolumna grupująca staje się naturalnym identyfikatorem wiersza,
# czyli indeksem.

# 4️⃣ Co się stanie jeśli zrobisz: df.groupby("miasto").mean() a masz w DataFrame kolumny tekstowe?
# Pandas pominie kolumny nienumeryczne, a dla reszty kolumn wypisze srednie (np. wiek, zarobki).

# 🔹 BONUS – pytanie projektowe (typowe dla juniora). Masz plik CSV z 200 000 wierszy.
# Masz policzyć średnie zarobki per miasto i zapisać wynik do nowego pliku. Opisz:

# 1. Jak wczytasz dane?
# df = pd.read_csv("plik.csv")

# 2. Jak sprawdzisz czy nie ma braków?
# df.isna().sum()

# 3. Jak policzysz średnie zarobki per miasto?
# df2 = df.groupby("miasto")["zarobki"].mean()

# 4. Jak zapiszesz wynik?
# df2.to_csv("srednie_zarobki_miasto.csv") 