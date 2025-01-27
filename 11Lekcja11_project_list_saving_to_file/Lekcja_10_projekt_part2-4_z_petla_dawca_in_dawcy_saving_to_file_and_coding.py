# Lekcja_9_projekt_2
# Projekt losujacy ludziom z Madery 
# osoby do prezentow mikołjakowych

import random
import base64

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
            element_listy_bytes = element_listy.encode('utf-8')
            encoded_element_listy = base64.b64encode(element_listy_bytes)
            encoded_string = encoded_element_listy.decode('utf-8')
            with open(str(dawca)+'.txt', 'w') as plik:      # str(dawca)!!!
                plik.write("Hej, z tej strony Wiola. Poniżej osoba, którą wylosowałeś do prezentu mikołajkowego.\n")
                plik.write(encoded_string)
                plik.write("\n")
                plik.write("Aby odkodować szyfr, wejdź w ten link: https://www.base64decode.org/")
            odbiorcy.remove(losowy_odbiorca)

        while dawca == losowy_odbiorca:
            losowy_odbiorca = odbiorcy[random.randint(0,len(odbiorcy)-1)]
            if dawca != losowy_odbiorca:
                element_listy = str(dawca) + " -> " + str(losowy_odbiorca)
                element_listy_bytes = element_listy.encode('utf-8')
                encoded_element_listy = base64.b64encode(element_listy_bytes)
                encoded_string = encoded_element_listy.decode('utf-8')
                with open(str(dawca)+'.txt', 'w') as plik: 
                    plik.write("Hej, z tej strony Wiola. Poniżej osoba, którą wylosowałeś do prezentu mikołajkowego.\n")
                    plik.write(encoded_string)
                    plik.write("\n")
                    plik.write("Aby odkodować szyfr, wejdź w ten link: https://www.base64decode.org/")
                odbiorcy.remove(losowy_odbiorca)
                break  

losowanie(uczestnicy)