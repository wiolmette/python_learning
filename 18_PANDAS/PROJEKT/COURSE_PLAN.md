# Plan kursu

Plan jest rozpisany na 6 tygodni przy założeniu 3-5 godzin pracy tygodniowo. Można go też zrealizować szybciej jako intensywny mini-bootcamp.

## Główne założenia

- Priorytet: `pandas`.
- SQL ćwiczony lokalnie na `sqlite`.
- Każdy etap kończy się małym artefaktem: notebookiem, tabelą, funkcją albo krótkim raportem.
- Każdy tydzień ma sekcję "po co", żeby kursantka rozumiała sens zadania, a nie tylko wykonywała instrukcje.

## Tydzień 1: Zrozumienie danych i środowiska

### Cel

Wczytać dane, zobaczyć ich kształt i przygotować repo do pracy.

### Zakres

- pobranie datasetu,
- rozpoznanie tabel i relacji,
- szybki data audit,
- zapis pierwszych obserwacji.

### Po co

W realnej pracy analiza rzadko zaczyna się od modelu albo wykresu. Najpierw trzeba zrozumieć, co właściwie jest w danych, czego brakuje i jakie są ograniczenia.

### Efekt tygodnia

- opis datasetu,
- lista kluczowych tabel,
- lista problemów z jakością danych,
- pierwszy notebook eksploracyjny.

### Dokumentacja

- [pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [`DataFrame.info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [`DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)

## Tydzień 2: Czyszczenie danych w pandas

### Cel

Uporządkować dane tak, aby nadawały się do analizy.

### Zakres

- typy danych,
- daty i czas,
- brakujące wartości,
- duplikaty,
- podstawowe reguły walidacji.

### Po co

Duża część pracy analityka to nie "analiza końcowa", tylko doprowadzenie danych do stanu, w którym wynik jest wiarygodny.

### Efekt tygodnia

- czystsze tabele,
- lista podjętych decyzji czyszczących,
- funkcje lub notebook z transformacjami.

### Dokumentacja

- [pandas: missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas: working with text data](https://pandas.pydata.org/docs/user_guide/text.html)
- [pandas: time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)

## Tydzień 3: SQLite i podstawy architektury analitycznej

### Cel

Przenieść część danych do lokalnej bazy `sqlite` i zacząć łączyć `pandas` z SQL.

### Zakres

- zapis DataFrame do `sqlite`,
- proste zapytania SQL,
- porównanie: co wygodniej robić w `pandas`, a co w SQL,
- uporządkowanie struktury folderów.

### Po co

Nawet jeśli ktoś dziś pracuje głównie w notebooku, to w praktyce analitycznej dane prawie zawsze pochodzą z tabel. `sqlite` to bezpieczny i prosty sposób na ćwiczenie bez serwera.

### Efekt tygodnia

- plik `.db`,
- kilka zapytań SQL,
- opis relacji między tabelami,
- pierwsze decyzje architektoniczne w repo.

### Dokumentacja

- [sqlite Python tutorial](https://docs.python.org/3/library/sqlite3.html)
- [`pandas.DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [`pandas.read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
- [SQLite tutorial](https://www.sqlitetutorial.net/)

## Tydzień 4: Analiza i KPI

### Cel

Zamienić dane w odpowiedzi na konkretne pytania biznesowe.

### Zakres

- definicja KPI,
- `groupby`,
- agregacje,
- `pivot_table`,
- analiza trendów w czasie,
- segmentacja prostymi regułami.

### Po co

Analiza nie polega na mechanicznym liczeniu średnich. Najpierw trzeba określić, jaka metryka odpowiada na pytanie biznesowe i czy na pewno jest poprawnie zdefiniowana.

### Efekt tygodnia

- tabela KPI,
- 3-5 odpowiedzi na pytania biznesowe,
- wykresy lub tabele podsumowujące.

### Dokumentacja

- [pandas: group by](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [`pandas.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
- [`DataFrame.merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)

## Tydzień 5: Raportowanie i komunikacja

### Cel

Przygotować krótki raport końcowy z wnioskami, założeniami i ograniczeniami.

### Zakres

- opis pytań biznesowych,
- metodologia,
- najważniejsze wyniki,
- ograniczenia danych,
- rekomendacje.

### Po co

W pracy analitycznej wynik musi być czytelny dla innych. Dobra analiza to nie tylko poprawny kod, ale też zrozumiały przekaz.

### Efekt tygodnia

- gotowy raport w markdown lub notebooku,
- sekcja "co wiemy" i "czego nie wiemy".

### Dokumentacja

- [Jupyter documentation](https://docs.jupyter.org/en/latest/)
- [pandas plotting overview](https://pandas.pydata.org/docs/user_guide/visualization.html)

## Tydzień 6: Refactor i nawyki "bliżej produkcji"

### Cel

Uprościć notebook, wydzielić logikę do funkcji i zostawić repo w stanie czytelnym dla drugiej osoby.

### Zakres

- przeniesienie powtarzalnego kodu do `src/`,
- uproszczenie notebooka,
- opis struktury projektu,
- końcowa checklista jakości.

### Po co

To jest pierwszy krok do dobrych nawyków software'owych. Nawet prosty projekt staje się dużo bardziej wartościowy, jeśli jest uporządkowany i łatwy do zrozumienia.

### Efekt tygodnia

- czytelniejsze repo,
- mniej duplikacji,
- lepszy podział odpowiedzialności między plikami.

### Dokumentacja

- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python logging](https://docs.python.org/3/library/logging.html)
- [PEP 8](https://peps.python.org/pep-0008/)

## Ocena końcowa projektu

Projekt można uznać za udany, jeśli kursantka potrafi:

1. opisać dane i ich ograniczenia,
2. samodzielnie oczyścić podstawowe problemy jakości,
3. połączyć dane w `pandas`,
4. użyć `sqlite` do prostych zapytań,
5. zdefiniować i policzyć sensowne KPI,
6. przygotować zwięzły raport z wnioskami,
7. wyjaśnić, dlaczego kod lub analiza zostały podzielone na konkretne części.

## Rozszerzenia po kursie

- dodać dashboard w `streamlit`,
- dopisać testy do funkcji liczących KPI,
- porównać to samo zadanie w `pandas` i w SQL,
- zrobić prostą segmentację klientów,
- spróbować odtworzyć część pipeline'u jako powtarzalny skrypt.
