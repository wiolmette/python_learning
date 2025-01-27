# Napisz program, który odwróci wprowadzony przez 
# użytkownika łańcuch znaków, używając pętli for.
text = input("Wprowadz text ")
odwrocony = ""
for litera in text:
    odwrocony = litera + odwrocony
print(odwrocony)
# w tym zadaniu podczas iteracji np. po slowie Wiola
# zawsze dajemy kazda kolejna litere na poczatek
# a to co wczesniej bylo na koniec
# czyli np. dla W mamy odwrocony = W
# dla i mamy: i + W (iW)
# dla o mamy: o + iW (oiW) itd.

