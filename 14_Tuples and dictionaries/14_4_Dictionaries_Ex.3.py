# Masz listę słów (np. z wczytanego pliku, z inputu od użytkownika lub zdefiniowaną w kodzie), np.
list = ["kot", "pies", "kot", "papuga", "pies", "kot"]

# Napisz kod, który przekształci tę listę w słownik zawierający słowo i liczbę jego wystąpień.
# Wynikiem będzie np. {"kot": 3, "pies": 2, "papuga": 1}.
# Napisz funkcję count_words(word_list), zwracającą słownik z takimi zliczeniami.

slownik = {}

def count_words(word_list):
    for word in list:
        slownik[word] = list.count(word)
    print(slownik)

count_words(list)

# Wyświetl wynik w porządku rosnącym (lub malejącym) według liczby wystąpień.

# wartosci2 = sorted(slownik.values())
# klucze2 = slownik.keys()
# print(klucze2)
# print(wartosci2)

print(slownik.items())

lista = sorted(slownik.items(), key=lambda x: x[1])    # x = 1, iterujemy po 2 elemencie (tutaj klucz jest 1. a wartosc 2.)
print(lista)
print(type(lista))
slownik2 = dict(lista)
print(slownik2)
print(type(slownik2))

lista2 = sorted(slownik.items(), key=lambda x: x[1], reverse = True)
slownik3 = dict(lista2)
print(slownik3)


