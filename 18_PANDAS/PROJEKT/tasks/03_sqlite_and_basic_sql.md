# Zadanie 3: SQLite i podstawy SQL na lokalnej bazie

## Cel

Przećwiczyć pracę z SQL bez pełnego serwera i zrozumieć, jak `pandas` oraz SQL mogą się uzupełniać.

## Zadania

1. Utwórz lokalny plik bazy `sqlite`.
2. Zapisz do niej przynajmniej 2 oczyszczone tabele z `pandas`.
3. Napisz minimum 3 zapytania SQL:
   - liczba zamówień per miesiąc,
   - przychód per kategoria,
   - liczba klientów powracających.
4. Uruchom te zapytania z poziomu Pythona i wczytaj wynik z powrotem do `pandas`.
5. Porównaj w 3-5 zdaniach:
   - co wygodniej liczyło się w `pandas`,
   - co wygodniej liczyło się w SQL.

## Pytania pomocnicze

- Kiedy `groupby` jest wygodniejsze od SQL?
- Kiedy SQL daje czytelniejszy zapis?
- Czy zapis do bazy pomaga uporządkować myślenie o tabelach i relacjach?

## Efekt końcowy

- działający plik `.db`,
- kilka zapytań SQL w folderze `sql/` albo w notebooku,
- tabela z wynikami wczytana do `pandas`.

## Dlaczego to ćwiczenie jest ważne

W praktyce analitycznej bardzo często przechodzisz między światem tabel i światem DataFrame. `sqlite` to prosty sposób, by ćwiczyć ten przepływ lokalnie.

## Dokumentacja

- [Python `sqlite3`](https://docs.python.org/3/library/sqlite3.html)
- [`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [`read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

## Dodatkowe wyzwanie

Policz ten sam KPI w `pandas` i w SQL. Porównaj:

- liczbę linii,
- czytelność,
- ryzyko pomyłki.
