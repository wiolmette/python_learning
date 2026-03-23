# Zadanie 1: Setup i zrozumienie danych

## Cel

Przygotować środowisko pracy i zrozumieć, co dokładnie znajduje się w datasetcie.

## Zadania

1. Pobierz dataset i umieść pliki CSV w `data/`.
2. Otwórz 2-4 najważniejsze pliki w `pandas`.
3. Dla każdego pliku sprawdź:
   - liczbę wierszy i kolumn,
   - typy danych,
   - brakujące wartości,
   - duplikaty,
   - przykładowe rekordy.
4. Narysuj prostą mapę relacji między tabelami:
   - która tabela jest główna,
   - po jakich kluczach da się łączyć dane.
5. Zapisz 5 pierwszych obserwacji o jakości danych.

## Pytania pomocnicze

- Która tabela wygląda na centralną?
- Czy są kolumny, które wyglądają jak klucze?
- Czy daty są zapisane jako tekst?
- Czy są kolumny, które już teraz wyglądają podejrzanie?

## Efekt końcowy

Powinien powstać pierwszy notebook z eksploracją oraz krótka notatka:

- jakie pliki masz,
- do czego prawdopodobnie służą,
- jakie problemy widać od razu.

## Dlaczego to ćwiczenie jest ważne

Bez tego bardzo łatwo zacząć liczyć coś na złych kolumnach albo błędnie połączyć tabele. To etap, który później oszczędza dużo czasu.

## Dokumentacja

- [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [`DataFrame.head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)
- [`DataFrame.info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)

## Dodatkowe wyzwanie

Spróbuj napisać krótką tabelę "słownik danych", np.:

| Kolumna | Tabela | Moje rozumienie |
|---|---|---|
| `order_id` | `orders` | identyfikator zamówienia |
