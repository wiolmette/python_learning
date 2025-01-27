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

    for dawca in dawcy:
         
        losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
        
        if dawca != losowy_odbiorca:
            print(dawca, "->", losowy_odbiorca)
            odbiorcy.remove(losowy_odbiorca)

        while dawca == losowy_odbiorca:
            losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
            if dawca != losowy_odbiorca:
                print(dawca, "->", losowy_odbiorca)
                odbiorcy.remove(losowy_odbiorca)
                break
        
losowanie(uczestnicy)
