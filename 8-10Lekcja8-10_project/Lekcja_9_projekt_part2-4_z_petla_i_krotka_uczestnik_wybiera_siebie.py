# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random

Uczestnicy = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]
Uczestnicy2 = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]
# liczba uczestnikow = len(Uczestnicy)
# losowy_uczestnik = random.randint(0,len(Uczestnicy2))

def losowanie(Uczestnicy):
    for i in range(0, len(Uczestnicy)):
        losowy_uczestnik = random.randint(0,len(Uczestnicy2)-1)
        print(Uczestnicy[i], "->", Uczestnicy2[losowy_uczestnik])
        Uczestnicy2.pop(losowy_uczestnik)

losowanie(Uczestnicy)