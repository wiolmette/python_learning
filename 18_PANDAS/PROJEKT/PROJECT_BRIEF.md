# Brief projektu

## Temat

Mini system analityczny dla sklepu e-commerce oparty o CSV + `pandas` + `sqlite`.

## Sytuacja

Masz kilka plików CSV opisujących zamówienia, klientów, produkty i płatności. Twoim zadaniem jest przygotować z nich prosty zestaw analiz biznesowych.

Nie pracujesz na pełnym serwerze SQL. Masz do dyspozycji:

- Python,
- `pandas`,
- lokalną bazę `sqlite`,
- notebooki,
- markdown.

## Główne pytania biznesowe

Na końcu projektu odpowiedz przynajmniej na 5 pytań:

1. Jak zmienia się liczba zamówień w czasie?
2. Jak zmienia się przychód w czasie?
3. Które kategorie produktów sprzedają się najlepiej?
4. Ilu klientów wraca z kolejnym zamówieniem?
5. Jaka jest średnia wartość koszyka?

## Wymagania minimalne

- wczytanie danych z CSV,
- podstawowe czyszczenie danych,
- połączenie minimum 3 tabel,
- zapis przynajmniej jednej oczyszczonej tabeli do `sqlite`,
- minimum 3 zapytania SQL,
- policzenie minimum 5 KPI,
- końcowy raport w markdown albo notebooku.

## Wymagania "na plus"

- wydzielenie części logiki do plików w `src/`,
- porównanie obliczenia KPI w `pandas` i w SQL,
- własna checklista jakości danych,
- krótka sekcja z ograniczeniami i ryzykiem błędnej interpretacji.

## Jak myśleć o architekturze

To nie jest "duży system", ale warto ćwiczyć dobre rozdzielenie:

- `data/`: surowe i pośrednie dane,
- `notebooks/`: eksploracja i szybkie testy,
- `sql/`: zapytania do `sqlite`,
- `src/`: kod wielokrotnego użycia,
- `reports/`: gotowe wnioski.

## Dlaczego to ważne

To rozdzielenie pomaga odpowiedzieć na kilka pytań:

- gdzie kończy się eksploracja, a zaczyna powtarzalna logika,
- które kroki są jednorazowe, a które warto automatyzować,
- jak sprawić, żeby inna osoba mogła zrozumieć projekt bez czytania całego notebooka.

## Sugerowany rezultat końcowy

Jedna osoba z zewnątrz powinna po 5 minutach rozumieć:

- skąd wzięły się dane,
- jakie były główne problemy jakości,
- jakie KPI policzono,
- jakie są najważniejsze wnioski,
- gdzie znajdują się najważniejsze elementy repo.
