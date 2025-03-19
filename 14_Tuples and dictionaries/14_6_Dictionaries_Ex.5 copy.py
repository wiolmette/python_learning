contacts = {
    "Jan Kowalski": {"phone": "123123123", "email": "jan@example.com"},
    "Anna Nowak": {"phone": "987987987", "email": "anna@example.com"}
}

# ------------------------------------   

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

# ------------------------------------

def read():
    while True:
        try:
            kontakt = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz wyswietlic: ")
            print(kontakt + ":" + " ",contacts[kontakt])
            break
        except KeyError:
            print("Podano bledna nazwe kontaktu")

# ------------------------------------

def update():
    while True:
        kontakt2 = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz zaktualizowac: ")   
        if kontakt2 not in contacts.keys():
            print("Podano bledna nazwe kontaktu")

        elif kontakt2 in contacts.keys():
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

# ------------------------------------

def manage_contacts():
    while True:
        opcja = input("Wybierz co chcesz zrobic ze swoja lista kontaktow: 1 - utworz nowy, 2 - wyswietl kontakt, 3 - zaktualizuj kontakt, 4 - usun kontakt. Jesli chcesz wyjsc z managera kontaktow, napisz '5'. ")
        if opcja == "1":
            create()
        if opcja == "2":
            read()
        if opcja == "3":
            update()
        if opcja == "4":
            delete()
        if opcja == "5":
            break
            
manage_contacts()