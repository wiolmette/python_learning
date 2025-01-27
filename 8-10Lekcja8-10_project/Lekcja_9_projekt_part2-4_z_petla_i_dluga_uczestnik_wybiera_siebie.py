# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random

Uczestnicy = ["Wiola", "Konrad", "Julia", "Milena", "Marcin", "Patka", "Filip", "Tobiasz", "Piotr"]
Uczestnicy2 = ["Wiola", "Konrad", "Julia", "Milena", "Marcin", "Patka", "Filip", "Tobiasz", "Piotr"]
# liczba uczestnikow = len(Uczestnicy)
# losowy_uczestnik = random.randint(0,len(Uczestnicy2))

def losowanie(Uczestnicy):
    
    for i in range(0, len(Uczestnicy)):
        losowy_uczestnik = random.randint(0,len(Uczestnicy2)-1)
        
        if i != losowy_uczestnik:

            while Uczestnicy2[losowy_uczestnik] == "wylosowany":
                losowy_uczestnik2 = random.randint(0,len(Uczestnicy2)-1)
                if Uczestnicy2[losowy_uczestnik2] != "wylosowany":
                    print(Uczestnicy[i], "->", Uczestnicy2[losowy_uczestnik2])
                    Uczestnicy2[losowy_uczestnik2] = "wylosowany"
                    break

            while Uczestnicy2[losowy_uczestnik] != "wylosowany":
                print(Uczestnicy[i], "->", Uczestnicy2[losowy_uczestnik])
                Uczestnicy2[losowy_uczestnik] = "wylosowany"

        while i == losowy_uczestnik:
            losowy_uczestnik3 = random.randint(0,len(Uczestnicy2)-1)
            if i != losowy_uczestnik3 and Uczestnicy2[losowy_uczestnik3] != "wylosowany":
                print(Uczestnicy[i], "->", Uczestnicy2[losowy_uczestnik3])
                Uczestnicy2[losowy_uczestnik3] = "wylosowany"
                break

losowanie(Uczestnicy)
