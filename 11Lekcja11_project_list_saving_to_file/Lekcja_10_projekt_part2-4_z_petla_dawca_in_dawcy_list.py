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
    mikołajki = []

    for dawca in dawcy:

        losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
        
        if dawca != losowy_odbiorca:
            element_listy = str(dawca) + " -> " + str(losowy_odbiorca)      # ŁĄCZENIE STRINGÓW!!!
            mikołajki.append(element_listy)
            odbiorcy.remove(losowy_odbiorca)

        while dawca == losowy_odbiorca:
            losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
            if dawca != losowy_odbiorca:
                element_listy = str(dawca) + " -> " + str(losowy_odbiorca)
                mikołajki.append(element_listy)
                odbiorcy.remove(losowy_odbiorca)
                break
    print(mikołajki)   

losowanie(uczestnicy)