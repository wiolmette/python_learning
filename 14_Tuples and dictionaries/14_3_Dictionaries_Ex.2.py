# 2. a) Utwórz słownik, w którym klucze to nazwy owoców, a wartości to ich kolory

owoce = {"jabłko": "czerwony", "banan": "żółty", "kiwi": "zielony"}

# b) Napisz funkcję invert_dict(d), która zamienia klucze z wartościami.
# Załóżmy, że wartości w oryginalnym słowniku są unikalne (dzięki temu mogą być jednoznacznymi nowymi kluczami).

owoce["mandarynka"] = "pomaranczowy"

# owoce["pomaranczowy"] = "mandarynka"

print(owoce)

print(owoce.keys())
print(owoce.values())

klucze = owoce.keys()
wartosci = owoce.values()

owoce2 = {}

owoce2[wartosci] = klucze

print(owoce2)

owoce3 = {}

for (klucz, wartosc) in owoce.items():
    owoce3[wartosc] = klucz
print(owoce3)


# def invert_dict(d):

