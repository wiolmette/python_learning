# Folder `data`

Tu umieść dane wejściowe do projektu.

## Co powinno tu trafić

- surowe pliki CSV,
- ewentualnie ich mniejsze próbki do szybszych testów,
- opcjonalnie plik `sqlite`, jeśli chcesz go trzymać razem z danymi.

## Dobra praktyka

Jeżeli chcesz, rozdziel dane na dwa typy:

- `raw`: dane wejściowe bez zmian,
- `processed`: dane po czyszczeniu.

Na tym etapie nie trzeba tego automatyzować perfekcyjnie. Wystarczy świadomie rozróżniać:

- co jest oryginalnym wejściem,
- co zostało już przez Ciebie zmienione.
