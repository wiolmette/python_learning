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
    imie_nazwisko = imie + " " + nazwisko
    telefon = input("Telefon kontaktu: ")
    email = input("E-mail kontaktu: ")
    # print(imie_nazwisko)
    global telefon1 
    telefon1 = {"telefon": telefon}
    global email1 
    email1 = {"email": email}
    contacts[imie_nazwisko] = telefon1, email1
    print(contacts)

create()

# ------------------------------------

def read():
    kontakt = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz wyswietlic: ")
    print(kontakt + ":" + " ",contacts[kontakt])

read()

# ------------------------------------

# ZROBIC ZADANIE ZAGNIEZDZAJAC SLOWNIKI A NIE PISZAC KLUCZE JAKO STRINGI <STUPIDO> XD 
# DODAC WARUNKI CO W RAZIE BLEDNEGO NAPISANIA NP. IMIENIA CZY COS

def update():
    kontakt2 = input("Wprowadz imie i nazwisko kontaktu, ktory chcesz zaktualizowac: ")
    wybor_opcji = input("Czy chcesz zaktualizowac numer telefonu? Napisz 'tak' lub 'nie'. ")
    if wybor_opcji == "tak":    
        telefon2 = input("Telefon kontaktu: ")
        telefon3 = {"telefon": telefon2}
        contacts[kontakt2] = telefon3, email1
        wybor_opcji2 = input("Czy chcesz zaktualizowac rowniez adres email? Napisz 'tak' lub 'nie'. ")
        if wybor_opcji2 == "tak":
            email2 = input("E-mail kontaktu: ")
            email3 = {"email": email2}
            contacts[kontakt2] = telefon3, email3
    if wybor_opcji == "nie":
        wybor_opcji3 = input("Czy chcesz zaktualizowac adres email? Napisz 'tak' lub 'nie'. ") 
        if wybor_opcji3 == "tak":
            email2 = input("E-mail kontaktu: ")
            email3 = {"email": email2}
            contacts[kontakt2] = telefon1, email3
    print(contacts)

update()