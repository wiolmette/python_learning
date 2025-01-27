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
            element_listy = str(dawca) + " -> " + str(losowy_odbiorca)      # ŁĄCZENIE STRINGÓW!!!
            with open(str(dawca)+'.txt', 'w') as plik:      # str(dawca)!!!
                plik.write(element_listy)
            odbiorcy.remove(losowy_odbiorca)

        while dawca == losowy_odbiorca:
            losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
            if dawca != losowy_odbiorca:
                element_listy = str(dawca) + " -> " + str(losowy_odbiorca)
                with open(str(dawca)+'.txt', 'w') as plik: 
                    plik.write(element_listy)
                odbiorcy.remove(losowy_odbiorca)
                break  

losowanie(uczestnicy)