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
    telefon1 = {"telefon": telefon}
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