# zadanie

import json
import sys

zadania = []

def dodawanie():
    zadanie = input("Nadaj nazwe zadania: ")
    zadania.append(zadanie)
    print ("Lista zadań:", zadania)

def usuwanie():
    for i, element in enumerate(zadania):
        print(i, element) 
    try:
        usuwanie = int(input('Napisz numer zadania, które chcesz usunąć '))
        zadania.pop(usuwanie)
        print ("Lista zadań:", zadania)
    except ValueError:
        print("Takie zadanie nie istnieje")      

def wyswietlanie():
    print ("Lista zadań:", zadania)

def zapisywanie():
    with open ('tasks.json', 'w') as plik:
        json.dump(zadania, plik, indent=4)
    print("Lista zadan zostala zapisana do pliku tasks.json")     

def wczytywanie():    
    try:
        with open("tasks.json", "r") as plik:
            zadania = json.load(plik)
        print("Wczytane zadania:", zadania)
    except FileNotFoundError:
        print("Plik z zadaniami nie istnieje") 

def zamykanie():
    sys.exit()

while True:
    print('Dostepne opcje programu: ')
    print('1 - Dodawanie nowych zadań')
    print('2 - Usuwanie istniejących zadań')
    print('3 - Wyświetlanie wszystkich zadań')
    print('4 - Zapisanie listy zadań do pliku')
    print('5 - Wczytanie listy zadań z pliku')
    print('6 - Zakonczenie programu')
    opcja = int(input('Wybierz opcje programu: '))
    
    match opcja:
        
        case _ if opcja == 1:
            dodawanie()    

        case _ if opcja == 2:
            usuwanie()             

        case _ if opcja == 3:
            wyswietlanie()    
        
        case _ if opcja == 4:
            zapisywanie()

        case _ if opcja == 5:
            wczytywanie()

        case _ if opcja == 6:
            zamykanie()