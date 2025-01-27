# Zadania z Baczensokursu:
# Cel: Stwórz program w Pythonie, który będzie funkcjonował jako dziennik cytatów i 
# notatek, z opcjami dodawania i zapisywania informacji w różnych formatach.

# Krok 1: Przygotowanie Środowiska
# Stwórz plik o nazwie dziennik.txt, który będzie używany do zapisywania danych przez cały program.

# Krok 2: Zapis Cytatów
# Zaproś użytkownika do wprowadzenia trzech ulubionych cytatów. Zapisz każdy cytat w nowej 
# linii w dziennik.txt.

# Krok 3: Zapis Daty i Czasu
# Na początku każdego cytatu, zapisz w dziennik.txt bieżącą datę i godzinę. Użyj modułu 
# datetime do pobrania tych danych. Informacje o korzystaniu z tego modułu zasięgnij z dokumentacji.
# Przykład linijki: data, godzina - “tekst cytatu”

# Krok 4: Dopisywanie cytatów
# Dodaj możliwość dopisywania kolejnych linijek do dziennika, użytkownik po odpaleniu 
# programu będzie stawał przed wyborem: wpisywać cytaty od 0 czy dopisać do istniejącego pliku dziennik.txt

# Krok 5: W przypadku tworzenia nowego dziennika, uzytkownik sam wymysla nazwe pliku
# Zaimplementuj w nim exception handling jesli nazwa dziennika jest niepoprawna

import datetime
from datetime import datetime

with open ('dziennik.txt', 'w') as plik:
    cytat = input("Napisz pierwszy ze swoich trzech ulubionych cytatów ")
    cytat2 = input("Napisz drugi ze swoich trzech ulubionych cytatów ")
    cytat3 = input("Napisz trzeci ze swoich trzech ulubionych cytatów ")
    plik.write(f"{datetime.now()} - {cytat} \n{datetime.now()} - {cytat2} \n{datetime.now()} - {cytat3} \n")
    cytaty_kontynuacja = input("Jesli chcesz kontynuowac dziennik, wprowadz kolejny cytat. Jeśli nie - napisz 'nie' ")
    
if cytaty_kontynuacja != "nie":    
    with open ('dziennik.txt', 'a') as plik:  
        plik.write(f"{datetime.now()} - {cytaty_kontynuacja}")

cytaty_od_0 = input("Jesli chcesz utworzyc nowy dziennik cytatów, napisz cytat. W kolejnym kroku nadasz nazwe dziennika. Jeśli nie - napisz 'nie' ")
if cytaty_od_0 != "nie":
    try:
        nazwa_dziennika = input("Wprowadz nazwe dziennika ")
        with open (str(nazwa_dziennika)+'.txt', 'w') as plik:
            plik.write(f"{datetime.now()} - {cytaty_od_0}")
    except OSError:
        nazwa_dziennika = input("Wprowadz inna, poprawna nazwe dziennika ")
        with open (str(nazwa_dziennika)+'.txt', 'w') as plik:
            plik.write(f"{datetime.now()} - {cytaty_od_0}")