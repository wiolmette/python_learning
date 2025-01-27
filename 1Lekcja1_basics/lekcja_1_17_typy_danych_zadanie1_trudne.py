# Napisz funkcję, która przyjmuje tekst i zwraca słownik, 
# gdzie klucze to litery tekstu, a wartości to liczba ich wystąpień w tekście.
# for, dict, get, char
tekst = input("Opisz swój ulubiony widok ")
print(tekst)
pierwsza_litera = tekst[0]
print(pierwsza_litera)
piata_litera = tekst[4]
print(piata_litera)
for litera in tekst:            # litera
    print(litera)
my_dict = {tekst: len(tekst)}   # len - liczy l. znaków w tekście
a = len(tekst)
print("Liczba znakow w tekscie to", a)
print(my_dict)
print("Klucze:", my_dict.keys())
print("Wartości:", my_dict.values())
print(tekst[0], tekst[1])
my_dict2 = {tekst[0]: 1, tekst[1]: 2, tekst[2]: 3, tekst[3]: 4}
print(my_dict2)
# Uwaga! Gdy zrobie 'slownik', ktory ma same klucze to tak naprawde zbior (set)
# zbior i lista to nie to samo, bo w liscie kolejnosc nie jest losowa!
# w zbiorze kolejnosc elementow jest losowa, np.
my_set = {tekst[0], tekst[1], tekst[2], tekst[3]}
print(my_set)
# tekst.count(litera) - liczy liczbe wystapien danej litery w tekscie
my_dict3 = {tekst[0]: tekst.count(tekst[0]), tekst[1]: tekst.count(tekst[1]), tekst[2]: tekst.count(tekst[3]), tekst[3]: tekst.count(tekst[4])}
print(my_dict3)
for i in range(a):
    my_dict4 = {tekst[i]: tekst.count(tekst[i])}
    print(my_dict4)        