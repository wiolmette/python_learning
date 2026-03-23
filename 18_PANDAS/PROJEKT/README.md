# Kurs: Mini Analityka E-commerce

To repo jest szkieletem prostego kursu dla osoby uczącej się na junior data analyst / data scientist. Główny nacisk jest na `pandas`, ale projekt wprowadza też podstawy pracy z `sqlite`, organizacji repo, myślenia analitycznego i prostego "mini-pipeline'u".

Projekt nie wymaga serwera SQL. Wystarczy Python, `pandas` oraz lokalna baza `sqlite`.

## Cel projektu

Zbudować mały system analityczny oparty o pliki CSV:

1. wczytać dane,
2. oczyścić je i ujednolicić,
3. zapisać wybrane tabele do `sqlite`,
4. policzyć najważniejsze KPI,
5. przygotować krótki raport z wnioskami.

## Dlaczego taki projekt

- Jest praktyczny: przypomina realną pracę analityczną.
- Daje dużo okazji do ćwiczenia `pandas`: `merge`, `groupby`, daty, brakujące wartości, `pivot_table`.
- Pozwala dalej używać SQL bez pełnego serwera.
- Pokazuje, po co rozdzielać eksplorację, logikę i raport.

## Proponowany dataset

Najwygodniej użyć jednego z publicznych datasetów e-commerce, np.:

- [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Jeżeli dataset okaże się za duży, można zacząć od próbki kilku plików CSV.

## Jak korzystać z repo

1. Zacznij od `COURSE_PLAN.md`.
2. Potem przeczytaj `START_HERE.md`.
3. Realizuj zadania w folderze `tasks/` po kolei.
4. Po każdym etapie zapisuj wnioski i pytania w swoim notebooku albo w osobnym pliku markdown.

## Proponowana struktura pracy

```text
.
├── COURSE_PLAN.md
├── PROJECT_BRIEF.md
├── START_HERE.md
├── data/
│   └── README.md
├── notebooks/
│   └── README.md
├── reports/
│   └── README.md
├── sql/
│   └── README.md
├── src/
│   └── README.md
└── tasks/
    ├── 01_setup_and_data_understanding.md
    ├── 02_cleaning_with_pandas.md
    ├── 03_sqlite_and_basic_sql.md
    ├── 04_analysis_and_kpis.md
    └── 05_final_report_and_refactor.md
```

## Czego kursantka ma się nauczyć

- swobodniejszej pracy w `pandas`,
- myślenia: "jakie pytanie biznesowe rozwiązuję?",
- podstaw organizacji projektu analitycznego,
- używania `sqlite` jako lekkiego środowiska do ćwiczenia SQL,
- oddzielania eksperymentów w notebooku od kodu wielokrotnego użycia.

## Ważna zasada

Nie chodzi o "zrobienie ładnych wykresów". Chodzi o zbudowanie prostego, czytelnego procesu:

- dane wejściowe,
- czyszczenie,
- transformacje,
- metryki,
- wnioski.

Taki sposób pracy skaluje się dużo lepiej niż pojedynczy chaotyczny notebook.
