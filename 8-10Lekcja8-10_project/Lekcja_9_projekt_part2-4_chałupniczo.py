# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random

Uczestnicy = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]
Uczestnicy2 = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]
# liczba_uczestnikow = len(Uczestnicy2)
# losowy_uczestnik = random.randint(1,len(Uczestnicy2))

def losowanie(Uczestnicy):
    
    losowy_uczestnik1 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[0], "->", Uczestnicy2[losowy_uczestnik1])
    Uczestnicy2.pop(losowy_uczestnik1)

    losowy_uczestnik2 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[1], "->", Uczestnicy2[losowy_uczestnik2])
    Uczestnicy2.pop(losowy_uczestnik2)
    
    losowy_uczestnik3 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[2], "->", Uczestnicy2[losowy_uczestnik3])
    Uczestnicy2.pop(losowy_uczestnik3)

    losowy_uczestnik4 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[3], "->", Uczestnicy2[losowy_uczestnik4])
    Uczestnicy2.pop(losowy_uczestnik4)

    losowy_uczestnik5 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[4], "->", Uczestnicy2[losowy_uczestnik5])
    Uczestnicy2.pop(losowy_uczestnik5)

    losowy_uczestnik6 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[5], "->", Uczestnicy2[losowy_uczestnik6])
    Uczestnicy2.pop(losowy_uczestnik6)

    losowy_uczestnik7 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[6], "->", Uczestnicy2[losowy_uczestnik7])
    Uczestnicy2.pop(losowy_uczestnik7)

    losowy_uczestnik8 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[7], "->", Uczestnicy2[losowy_uczestnik8])
    Uczestnicy2.pop(losowy_uczestnik8)

    losowy_uczestnik9 = random.randint(0,len(Uczestnicy2)-1)
    print(Uczestnicy[8], "->", Uczestnicy2[losowy_uczestnik9])
    Uczestnicy2.pop(losowy_uczestnik9)

losowanie(Uczestnicy)
