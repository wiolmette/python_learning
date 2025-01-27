# Zadanie 1: Napisz pętlę for, która wypisze wszystkie 
# liczby od 1 do 10. Użyj range().
for i in range(10):
    print(i+1)

# TEORIA DODATKOWA
# break – pozwala na przerwanie działania pętli przed jej naturalnym zakończeniem
for liczba in range(10):
    if liczba == 5:
        break
    print(liczba)

# continue – pomija bieżącą iterację pętli i przechodzi do następnej
for liczba in range(5):
    if liczba == 2:
        continue
    print(liczba)

# else w pętlach – blok else w pętli wykona się tylko wtedy, 
# gdy pętla zakończy się naturalnie, tzn. nie zostanie przerwana przez break
for liczba in range(5):
    print(liczba)
else:
    print("Pętla zakończona")

# przyklad z break i else
for liczba in range(5):
    if liczba == 3:
        break
    print(liczba)
else:
    print("Pętla zakończona")