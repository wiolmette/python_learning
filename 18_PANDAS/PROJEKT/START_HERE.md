# Start here

Ten plik ma pomóc kursantce ruszyć bez zgadywania, od czego zacząć.

## Minimalne środowisko

- Python 3.10+ albo nowszy,
- `pandas`,
- Jupyter Notebook albo JupyterLab,
- standardowa biblioteka Pythona z modułem `sqlite3`.

## Szybki start

1. Przeczytaj `PROJECT_BRIEF.md`.
2. Pobierz dataset i umieść pliki CSV w `data/`.
3. Załóż pierwszy notebook w `notebooks/`.
4. Zrealizuj zadanie z `tasks/01_setup_and_data_understanding.md`.

## Jak pracować

Przy każdym etapie zadawaj sobie te pytania:

1. Co próbuję zrozumieć?
2. Skąd wiem, że dane są wystarczająco dobre do tego kroku?
3. Czy ten kod będzie jednorazowy, czy warto go wydzielić?
4. Jak wytłumaczę tę decyzję komuś innemu?

## Jak korzystać z pandas i SQL razem

Najprostszy model pracy:

- `pandas` do wczytywania, czyszczenia i szybkiej eksploracji,
- `sqlite` do ćwiczenia zapytań SQL i prostych agregacji,
- markdown do opisu wniosków i decyzji.

## Gdzie szukać pomocy

- oficjalna dokumentacja `pandas`: [user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- dokumentacja `sqlite3` w Pythonie: [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- tutorial SQL dla SQLite: [SQLite Tutorial](https://www.sqlitetutorial.net/)

## Dobra praktyka

Jeśli jakiś krok wydaje się "tylko techniczny", spróbuj dopisać jedno zdanie:

> Robię to, ponieważ ...

To pomaga budować nawyk tłumaczenia decyzji analitycznych i projektowych.
