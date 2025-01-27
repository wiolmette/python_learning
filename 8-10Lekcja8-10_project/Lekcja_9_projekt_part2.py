# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random

Uczestnicy = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]
Uczestnicy2 = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]

# len(Uczestnicy) - liczba elementow listy uczestnicy

def losowanie(Uczestnicy):
    liczba_uczestnikow = len(Uczestnicy)
    losowy_uczestnik = random.randint(1,liczba_uczestnikow+1)
    Uczestnicy3 = []
    for Uczestnik in Uczestnicy:
        print(Uczestnik, "+", Uczestnicy2[losowy_uczestnik])
    Uczestnicy2.pop(losowy_uczestnik)
    print(Uczestnicy2) 
    

losowanie(Uczestnicy)