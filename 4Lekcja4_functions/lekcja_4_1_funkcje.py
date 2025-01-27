# Funkcja która dodaje 2 liczby
def dodawanie(x, y):
    return x+y
suma = dodawanie(1,4)
print(suma)

# W funkcjach uzywać return zamiast print bo wtedy mozna uzyc wyniku funkcji tez poza ta funkcja
# Normalnie zmienne definiowane w danej funkji istnieja tylko w niej
# return konczy dzialanie funkcji

def dodawanie(a, b):
    print("Teraz się wykonuje dodawanie bez return")
    print(a+b)
    c = a+b

def dodawanie_z_return(a,b):
    print("Teraz wykonuje się dodawanie z return")
    print(a+b)
    return(a+b)

def odejmij_dwa(a):
    print("Teraz wykonuje się odejmowanie")
    return a-2

dodawanie(4,2)
print(odejmij_dwa(dodawanie_z_return(12, 10)))     # Nie mozna zastapic print(odejmij_dwa(c)) !!!

wynik = dodawanie_z_return(5, 2)
print(wynik)