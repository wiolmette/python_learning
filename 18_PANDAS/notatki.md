# 📊 Pandas – szybka ściągawka (Junior Data Analyst)

---

## 1️⃣ Podstawowe obiekty

### 🔹 Series

- jednowymiarowa struktura danych  
- ma indeks  
- tworzona z listy, dicta, numpy array  

```python
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
```

**Najważniejsze funkcje:**

- `s.mean()` – średnia z Series  
- `s.sum()` – suma  
- `s.unique()` – zwraca wszystkie unikalne wartości  
- `s.nunique()` – zwraca liczbę unikalnych wartości  

---

### 🔹 DataFrame

- tabela 2D  
- kolumny mogą mieć różne typy  

```python
df = pd.DataFrame({
    "wiek": [20, 30],
    "miasto": ["Gdańsk", "Warszawa"]
})
```

---

## 2️⃣ Wczytywanie danych

### 🔹 CSV

```python
pd.read_csv("plik.csv")
```

**Ważne parametry:**

- `sep` – określa separator kolumn  
  ```python
  df = pd.read_csv("plik.csv", sep=";")
  ```

- `header` – określa, który wiersz zawiera nazwy kolumn  
  ```python
  df = pd.read_csv("plik.csv", header=0)      # pierwszy wiersz to nagłówki
  df = pd.read_csv("plik.csv", header=None)   # brak nagłówków
  ```

- `index_col` – ustawia kolumnę jako indeks  
  ```python
  df = pd.read_csv("plik.csv", index_col=0)
  df = pd.read_csv("plik.csv", index_col="NAZWA_KOLUMNY")
  ```

- `encoding` – określa kodowanie znaków  
  ```python
  df = pd.read_csv("plik.csv", encoding="utf-8")
  ```

---

### 🔹 JSON

```python
pd.read_json("plik.json")
```

---

## 3️⃣ Szybkie poznanie danych (must-have)

```python
df.head(WARTOŚĆ)
df.tail(WARTOŚĆ)
df.shape
len(df)
df.columns
df.dtypes
df.info()
df.describe()
```

### 🔹 Co zwracają?

- `df.head()` – nagłówki + 5 pierwszych wierszy  
- `df.head(10)` – nagłówki + 10 pierwszych wierszy  
- `df.tail()` – 5 ostatnich wierszy  
- `df.shape` – `(liczba_wierszy, liczba_kolumn)`  
- `len(df)` – liczba wierszy (jak `df.shape[0]`)  
- `df.columns` – nazwy kolumn  
- `df.dtypes` – typy kolumn  

---

### 🔹 `df.info()` pokazuje:

- liczbę wierszy  
- nazwy kolumn  
- liczbę niepustych wartości  
- typ każdej kolumny  
- zużycie pamięci  

Używane do szybkiego wykrywania braków danych i złych typów.

---

### 🔹 `df.describe()` (dla kolumn liczbowych)

Zwraca:

- `count` – liczba wartości ≠ NaN  
  ```python
  df["NAZWA_KOLUMNY"].count()
  ```

- `mean` – średnia  
- `std` – odchylenie standardowe  
- `min` – wartość minimalna  
- `25%` – wartość, poniżej której znajduje się 25% obserwacji  
  ```python
  df.quantile(0.25)
  ```

- `50%` – mediana  
  ```python
  df["NAZWA_KOLUMNY"].median()
  ```

- `75%` – trzeci kwartyl  
- `max` – wartość maksymalna  

---

### Junior musi wiedzieć, czym różni się:

- `info()` vs `describe()`  
- `shape` vs `count()`  

---

## 4️⃣ Wybieranie danych

### 🔹 Kolumny

```python
df["wiek"]
df[["wiek", "miasto"]]
```

---

### 🔹 Wiersze

#### `.loc` (po nazwach / warunkach)

```python
df.loc[0]
df.loc[df["wiek"] > 30]
```

#### `.iloc` (po indeksach liczbowych)

```python
df.iloc[0]
df.iloc[0:5]
```

Bardzo częste pytanie rekrutacyjne: różnica `loc` vs `iloc`.

---

## 5️⃣ Filtrowanie (mega ważne)

```python
df[df["wiek"] > 30]
```

Kilka warunków:

```python
df[(df["wiek"] > 30) & (df["miasto"] == "Gdańsk")]
```

---

## 6️⃣ Operacje na kolumnach

### 🔹 Dodawanie kolumn

```python
df["nowa_kolumna"] = warunek
df["pełnoletni"] = df["wiek"] >= 18
```

Dodaje kolumnę typu `True/False`.

---

### 🔹 Usuwanie

```python
df.drop(columns=["wiek"])
```

---

### 🔹 Zmiana nazw

```python
df.rename(columns={"wiek": "age"})
```

---

## 7️⃣ Typy danych

### 🔹 Komenda zwracajaca typy danych w kolumnach

```python
df.dtypes
```
### 🔹 Komenda zamieniajaca zamienia kolumnę "data" na typ daty
```python
df["data"] = pd.to_datetime(df["data"])
```
### 🔹 Komenda zamiany typu kolumny "wiek" na liczbę calkowita
```python
df["wiek"] = df["wiek"].astype(int)
```

Junior powinien wiedzieć:

- `object` ≠ liczba  
*(roznica: obiekt to tekst i nie mozna na nim wykonywac operacji matematycznych)*
- daty mają typ `datetime64[ns]`  

---

## 8️⃣ Braki danych (NaN)

### 🔹 Pokazywanie gdzie sa braki danych

```python
df.isna()   
```
True → w tym miejscu jest brak danych

False → wartość istnieje

```python
df.isna().sum()     
```
Liczy ile jest brakow danych w kazdej kolumnie


### 🔹 Usuwanie

```python
df.dropna(subset=['Nazwa_kolumny'])
```
Usuwa puste wiersze (subset - w zadanej kolumnie)

### 🔹 Uzupełnianie

```python
df.fillna(0)
df["wiek"].fillna(df["wiek"].mean())
```
uzupelnia puste komorki kolumny wiek 0 \ srednimi (mean)

---

## 9️⃣ Czyszczenie błędnych danych

Maski logiczne:

```python
df.loc[df["wiek"] > 120, "wiek"] = 120
```
dla komorek kolumny "wiek" powyzej 120, zamienia wartosc na 120

Lub:

```python
df["wiek"] = df["wiek"].clip(upper=120)
```
obcinanie wartosci powyzej 120

---

## 🔟 Duplikaty

```python
df.duplicated()         # pokazuje zduplikowane wiersze
df.drop_duplicates()    # usuwa duplikaty
```

---

## 1️⃣1️⃣ Sortowanie

```python
df.sort_values("wiek")                  # sortowanie rosnoca
df.sort_values("wiek", ascending=False) # malejaco
df.sort_index()                         # sortuje wg indeksu
```

---

## 1️⃣2️⃣ Statystyki opisowe

```python
df.mean()
df.sum()
df.min()
df.max()
df.count()
df.nunique()
```

Różnica:

- `count()` → liczba niepustych wartości  
- `nunique()` → liczba wartości unikalnych  

---

## 1️⃣3️⃣ Korelacje

```python
df.corr()
```

Junior powinien:

- wiedzieć, że domyślnie to korelacja Pearsona  
- umieć wskazać najsilniejszą korelację  
- nie interpretować korelacji jako przyczynowości  

---

## 1️⃣4️⃣ Grupowanie (bardzo często wymagane)

```python
df.groupby("miasto")["wiek"].mean()

df.groupby("miasto").agg({
    "wiek": "mean",
    "Calories": "sum"
})
```

---

## 1️⃣5️⃣ Wykresy

```python
df.plot(kind="line")
df.plot(kind="bar")
df["wiek"].plot(kind="hist")
df.plot(x="Duration", y="Calories", kind="scatter")
```

Junior musi rozróżniać:

- `bar` vs `hist`  
- `line` vs `scatter`  

---

## 1️⃣6️⃣ Indeks

- indeks ≠ kolumna  
- można go resetować  

```python
df.reset_index(drop=True)
```
