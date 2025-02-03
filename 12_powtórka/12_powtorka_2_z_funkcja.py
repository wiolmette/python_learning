# zadanie

k = 1

def co_nastepnie():
    co_dalej = int(input('Chcesz zamknac program (6) czy kontynuowac (7)? '))
    if co_dalej == 6:
        k = 2
    if co_dalej == 7:
        k = 1

while k == 1:
    print('Dostepne opcje programu: ')
    print('1 - Dodawanie nowych zadań')
    print('2 - Usuwanie istniejących zadań')
    print('3 - Wyświetlanie wszystkich zadań')
    print('4 - Zapisanie listy zadań do pliku')
    print('5 - Wczytanie listy zadań z pliku')
    opcja = int(input('Wybierz opcje programu: '))
    zadania = []

    if opcja == 1:
        zadanie = input("Nadaj nazwe zadania: ")
        zadania.append(zadanie)
        print ("Lista zadań:", zadania)
        co_nastepnie()
        print(k)

    if opcja == 2:
        for i, element in enumerate(zadania):
            print(i, element)
        usuwanie = int(input('Napisz numer zadania, które chcesz usunąć '))
        if usuwanie == 1:
            zadania.pop(0)
        print ("Lista zadań:", zadania)
        co_nastepnie()

    if k == 2:
        break