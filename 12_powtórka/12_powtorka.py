# zadanie

while True:
    print('Dostepne opcje programu: ')
    print('1 - Dodawanie nowych zadań')
    print('2 - Usuwanie istniejących zadań')
    print('3 - Wyświetlanie wszystkich zadań')
    print('4 - Zapisanie listy zadań do pliku')
    print('5 - Wczytanie listy zadań z pliku')
    opcja = int(input('Wybierz opcje programu: '))
    zadania = []
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
        usuwanie = int(input('Napisz numer zadania, które chcesz usunąć '))
        if usuwanie == 0:
            zadania.pop(0)
        print ("Lista zadań:", zadania)
    break