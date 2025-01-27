# for - ptetla wykorzystywana do iteracji po sekwencjach 
# (listach, krotkach, słownikach, itp.).

# SKLADNIA
# for element in sekwencja:
    # blok kodu

for i in range(5): #tylko integery czyli l. calkowite
    print("Liczba:", i)

text = "Hello world!"
for znak in text:
    print(znak)

lista_owoce = ('jablko', 'gruszka', 'kiwi') # element to moze byc dowolne slowo!
for owoc in lista_owoce:                    # program rozumie, ze np. elementami   
    print(owoc)                             # listy sa dane slowa 
                                            # a elementami slowa sa litery itd.


