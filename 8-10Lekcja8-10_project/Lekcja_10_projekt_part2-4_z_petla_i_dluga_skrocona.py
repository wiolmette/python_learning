# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random

uczestnicy = ["Wiola", "Konrad", "Julia", "Milena", "Marcin", "Patka", "Filip", "Tobiasz", "Piotr"]
# liczba uczestnikow = len(Uczestnicy)
# losowy_uczestnik = random.randint(0,len(Uczestnicy2))

def losowanie(uczestnicy):

    dawcy = uczestnicy
    odbiorcy = uczestnicy.copy()
    
    for i in range(0, len(dawcy)):
       
        losowy_odbiorca = random.randint(0,len(odbiorcy)-1)

        if dawcy[i] != odbiorcy[losowy_odbiorca]:
            print(dawcy[i], "->", odbiorcy[losowy_odbiorca])
            odbiorcy.remove(odbiorcy[losowy_odbiorca])

        elif dawcy[i] == odbiorcy[losowy_odbiorca]:
            while True:
                losowy_odbiorca = random.randint(0,len(odbiorcy)-1)
                if dawcy[i] != odbiorcy[losowy_odbiorca]:
                    print(dawcy[i], "->", odbiorcy[losowy_odbiorca])
                    odbiorcy.remove(odbiorcy[losowy_odbiorca])
                    break
        
losowanie(uczestnicy)
