# match and case - Instrukcja match opiera się na wzorcach, 
# które mogą być dopasowane do wartości. Wykorzystuje ona 
# słowo kluczowe case do zdefiniowania różnych przypadków.

# Składnia:
# match wartość:
    # case wzorzec1:        (kod do wykonania, gdy wzorzec1 pasuje)
    # case wzorzec2:        (kod do wykonania, gdy wzorzec2 pasuje)
    # case _:               (kod do wykonania, gdy żaden wzorzec nie pasuje, opcjonalnie)
                            # "_" to underscore (podkreślnik)

# Przykład
day = "wtorek"
match day:
    case "poniedziałek":
        print("To jest początek tygodnia!")
    case "wtorek":
        print("Drugi dzień tygodnia.")
    case "środa":
        print("Już bliżej do weekendu!")
    case _:
        print("Inny dzień tygodnia.")

# Do case mozna tez dawac np. if
wiek = 20

match wiek:
    case _ if wiek < 18:
        print("Osoba jest niepełnoletnia")
    case _ if 18 <= wiek <= 65:
        print("Osoba jest dorosła")
    case _:
        print("Osoba jest seniorem")

