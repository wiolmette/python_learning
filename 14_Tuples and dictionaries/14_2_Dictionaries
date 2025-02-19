# 1.
# a) Napisz funkcję count_letters(text), która przyjmuje łańcuch znaków (string) i 
# zwraca słownik, w którym kluczem jest każda występująca litera, a wartością – 
# liczba jej wystąpień w tekście.

import re

text1 = "Baczens kocha Dupensa"
slownik = {}

def count_letters(text):
    for letter in text:
        slownik[letter] = text.count(letter)
    print(slownik)

# count_letters(text1)

# b)
text2 = "Dupka dupka"
# count_letters(text2)

# c) (Opcjonalnie) Zwracaj tylko litery a–z (ignoruj inne znaki). 
# Możesz zrealizować to, np. konwertując tekst do małych liter i odfiltrowując te spoza zakresu.

text3 = re.sub(r'[^a-z]', '', text2.lower())
print(text3)
count_letters(text3)

