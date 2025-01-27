# Projekt losujacy ludziom z Madery osoby do prezentow mikołjakowych

import random

# Uczestnicy = ["Wiola", "Konrad", "Milena", "Marcin", "Patka", "Filip", "Julia", "Tobiasz", "Piotr"]

Uczestnicy1 = []
for i in range (1,3):
    Uczestnicy1.append(random.randint(1,9))
    i = i + 1
print(Uczestnicy1)

if Uczestnicy1[0] == Uczestnicy1[1]:
    Uczestnicy1[1] = random.randint(1,9)

print(Uczestnicy1)


for j in range (1,10):
    k = random.randint(1,9)
    if j == k:
        k = random.randint(1,9)
    print(j, k)
    j = j + 1

    