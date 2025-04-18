# Zad. 5 Słownik kontaktów (CRUD)
# Zbuduj prosty system zarządzania kontaktami, przechowujący dane w słowniku:

contacts = {
    "Jan Kowalski": {"phone": "123123123", "email": "jan@example.com"},
    "Anna Nowak": {"phone": "987987987", "email": "anna@example.com"}
}

# 1. Zaimplementuj w funkcji manage_contacts() lub w osobnym module:
# Create: Dodawanie nowego kontaktu (zapytaj o imię, nazwisko, telefon, e-mail).
# Read: Wyświetlanie danych wybranego kontaktu.
# Update: Aktualizacja istniejącego kontaktu (np. zmiana telefonu).
# Delete: Usunięcie kontaktu po imieniu i nazwisku.

# kolor = input("podaj kolor buraka ")
# burak = {"burak": kolor}
# print(burak)

def create():
    imie = input("Imie kontaktu: ")
    nazwisko = input("Nazwisko kontaktu: ")
    global imie_nazwisko
    imie_nazwisko = imie + " " + nazwisko
    telefon = input("Telefon kontaktu: ")
    email = input("E-mail kontaktu: ")
    print(imie_nazwisko)
    global telefon1 
    telefon1 = {"telefon": telefon}
    global email1 
    email1 = {"email": email}
    contacts[imie_nazwisko] = telefon1, email1
    print(contacts)

create()

# ------------------------------------

def read():
    while True:
        try:
            kontakt = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz wyswietlic: ")
            print(kontakt + ":" + " ",contacts[kontakt])
            break
        except KeyError:
            print("Podano bledna nazwe kontaktu")


read()

# ------------------------------------

def update():
    while True:
        kontakt2 = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz zaktualizowac: ")   
        if kontakt2 not in ["Jan Kowalski", "Anna Nowak", imie_nazwisko]:
            print("Podano bledna nazwe kontaktu")

        elif kontakt2 in ["Jan Kowalski", "Anna Nowak", imie_nazwisko]:
            while True:
                wybor_opcji = input("Podaj dane do zaktualizowania? 1 - telefon, 2 - email, 3 - telefon i email. Napisz '1', '2' lub '3'. ")
                if wybor_opcji not in ["1", "2", "3"]:
                    print("Prosze wpisac '1', '2' lub '3' ")

                if wybor_opcji == "1":    
                    telefon2 = input("Telefon kontaktu: ")
                    telefon3 = {"telefon": telefon2}
                    contacts[kontakt2] = telefon3, email1
                    print(contacts)
                    return
                                
                if wybor_opcji == "2":    
                    email2 = input("E-mail kontaktu: ")
                    email3 = {"email": email2}
                    contacts[kontakt2] = telefon1, email3
                    print(contacts)
                    return
                                
                if wybor_opcji == "3":
                    telefon2 = input("Telefon kontaktu: ")
                    telefon3 = {"telefon": telefon2}
                    email2 = input("E-mail kontaktu: ")
                    email3 = {"email": email2}
                    contacts[kontakt2] = telefon3, email3
                    print(contacts)
                    return

update()

# ROBIAC FUNKCJE GLOWNA ZROBIC PORZADEK ZE ZMIENNYMI LOK/GLOB!

# ------------------------------------

def delete():
    while True:
        try:
            kontakt3 = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz usunac: ")
            del contacts[kontakt3]
            break
        except KeyError:
            print("Podano bledna nazwe kontaktu")
    print(contacts)

delete()



