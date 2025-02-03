# zadanie

import json

zadania = []

while True:
    print('Dostepne opcje programu: ')
    print('1 - Dodawanie nowych zadań')
    print('2 - Usuwanie istniejących zadań')
    print('3 - Wyświetlanie wszystkich zadań')
    print('4 - Zapisanie listy zadań do pliku')
    print('5 - Wczytanie listy zadań z pliku')
    opcja = int(input('Wybierz opcje programu: '))
    
    while opcja == 1:
        zadanie = input("Nadaj nazwe zadania: ")
        zadania.append(zadanie)
        print ("Lista zadań:", zadania)
        co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
        if co_dalej == 6:
            break
        if co_dalej == 7:
            opcja = int(input('Wybierz kolejna opcje programu: '))
    

    if opcja == 2:
        for i, element in enumerate(zadania):
            print(i, element) 
        try:
            usuwanie = int(input('Napisz numer zadania, które chcesz usunąć '))
            zadania.pop(usuwanie)
            print ("Lista zadań:", zadania)
        except ValueError:
            print("Takie zadanie nie istnieje")

        co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
        if co_dalej == 6:
            break
        if co_dalej == 7:
            opcja = int(input('Wybierz kolejna opcje programu: '))
    

    if opcja == 3:
        print ("Lista zadań:", zadania)
        co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
        if co_dalej == 6:
            break
        if co_dalej == 7:
            opcja = int(input('Wybierz kolejna opcje programu: '))
    

    if opcja == 4:
        with open ('tasks.json', 'w') as plik:
           json.dump(zadania, plik, indent=4)
        print("Lista zadan zostala zapisana do pliku tasks.json") 
        co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
        if co_dalej == 6:
            break
        if co_dalej == 7:
            opcja = int(input('Wybierz kolejna opcje programu: '))
    

    if opcja == 5:
        try:
            with open("tasks.json", "r") as plik:
                zadania = json.load(plik)
            print("Wczytane zadania:", zadania)
        except FileNotFoundError:
            print("Plik z zadaniami nie istnieje") 
        
        co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
        if co_dalej == 6:
            break
        if co_dalej == 7:
            print("Powrot do glownego menu")