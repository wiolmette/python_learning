# Zadanie 2: Czyszczenie danych w pandas

## Cel

Doprowadzić dane do stanu, w którym można je bezpiecznie łączyć i analizować.

## Zadania

1. Wybierz 2-3 najważniejsze tabele do czyszczenia.
2. Sprawdź i popraw:
   - typy danych,
   - format dat,
   - brakujące wartości,
   - duplikaty,
   - niespójne nazwy kategorii lub statusów.
3. Zapisz wszystkie decyzje czyszczące:
   - co zmieniasz,
   - dlaczego,
   - jaki może to mieć wpływ na analizę.
4. Po czyszczeniu wykonaj proste sanity checks:
   - czy liczba rekordów ma sens,
   - czy klucze nadal są unikalne,
   - czy daty mieszczą się w sensownym zakresie.

## Pytania pomocnicze

- Które `NaN` można uzupełnić, a które lepiej zostawić?
- Czy usunięcie duplikatu jest na pewno bezpieczne?
- Czy zmiana typu nie ukrywa błędu w danych?

## Efekt końcowy

- notebook lub skrypt z czyszczeniem,
- lista decyzji czyszczących,
- oczyszczone DataFrame gotowe do łączenia.

## Dlaczego to ćwiczenie jest ważne

To właśnie tutaj buduje się wiarygodność analizy. Jeśli ten etap jest słaby, późniejsze KPI mogą wyglądać dobrze, ale być po prostu błędne.

## Dokumentacja

- [missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [time series](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
- [`drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html)
- [`astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)

## Dodatkowe wyzwanie

Wydziel co najmniej jedną funkcję do `src/`, np. funkcję czyszczącą jedną tabelę. Dzięki temu zaczniesz ćwiczyć oddzielanie kodu eksploracyjnego od kodu wielokrotnego użycia.
