# Zadanie 4: Analiza i KPI

## Cel

Przekształcić oczyszczone dane w odpowiedzi na konkretne pytania biznesowe.

## Zadania

1. Zdefiniuj minimum 5 KPI, np.:
   - liczba zamówień,
   - przychód,
   - średnia wartość koszyka,
   - liczba aktywnych klientów,
   - odsetek klientów powracających.
2. Dla każdego KPI dopisz:
   - jak liczysz metrykę,
   - z jakich tabel korzystasz,
   - jakie są założenia i ograniczenia.
3. Wykonaj analizę w przekrojach:
   - czas,
   - kategoria produktu,
   - status zamówienia,
   - klient nowy vs powracający.
4. Przygotuj 3-5 wykresów albo tabel podsumowujących.

## Pytania pomocnicze

- Czy KPI jest zdefiniowane jednoznacznie?
- Czy przychód oznacza wartość wszystkich zamówień, czy tylko zakończonych?
- Jak rozpoznajesz klienta powracającego?

## Efekt końcowy

- tabela KPI,
- odpowiedzi na pytania biznesowe,
- materiał do raportu końcowego.

## Dlaczego to ćwiczenie jest ważne

Tutaj zaczyna się prawdziwa analiza. Sama znajomość narzędzia nie wystarczy, jeśli nie wiadomo, jak przełożyć pytanie biznesowe na poprawną metrykę.

## Dokumentacja

- [groupby](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [`pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
- [`merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)

## Dodatkowe wyzwanie

Dodaj sekcję "ryzyka interpretacyjne", np.:

- brak części danych,
- niejednoznaczna definicja statusu,
- możliwe zaniżenie lub zawyżenie metryk.
