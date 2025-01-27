a = int(input("Podaj ile masz banknotów 10 zł "))
b = int(input("Podaj ile masz banknotów 20 zł "))
c = int(input("Podaj ile masz banknotów 50 zł "))
d = int(input("Podaj ile masz banknotów 100 zł "))
e = int(input("Podaj cenę produktu, który kupujesz "))
f = 10*a + 20*b +50*c + 100*d
reszta = f-e
print(f"Zostało Ci {reszta} reszty")