# Napisz funkcję, która przyjmuje tekst i zwraca słownik, 
# gdzie klucze to litery tekstu, a wartości to liczba ich wystąpień w tekście.
# for, dict, get, char
dictionary = {}
text = "Hello World"
for znak in text:       
    dictionary[znak]=dictionary.get(znak,0)+1
print(dictionary)

# get - pobiera wartosc przypisana do danego klucza ze slownika
# składnia: dictionary.get(key)
dictionary2 = {"Ala": 25, 5: 25}
print(dictionary2)
wartosc = dictionary2.get("Ala")
print(wartosc)

