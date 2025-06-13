# Zadanie 1 – polacz sie z API i pobierz dane

import requests
import json

response = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll')  # endpoint zaczyna sie od http i trzeba go dac w apostrofy!!!
data = response.json() 
print(data)
print(data['Lista stacji pomiarowych'])  # zle liczy, nie liczy liczby stacji
print(data['Lista stacji pomiarowych'])
print(len(data['Lista stacji pomiarowych']))

# Zadanie 2 - samodzielny wypis stacji
print(type(data['Lista stacji pomiarowych']))
lista_stacji = data['Lista stacji pomiarowych']
for i in range (0,10):
    print(lista_stacji[i]['Identyfikator stacji'], "-",  lista_stacji[i]['Nazwa stacji'], "(", lista_stacji[i]['Nazwa miasta'], ")")

# Zadanie 3 – Wyświetl sensory dla wybranej stacji
response1 = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/data/getData/52')     # Biezace dane pomiarowe
data1 = response1.json() 
print(data1)

response2 = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/aqindex/getIndex/52')     # Indeks jakosci powietrza
data2 = response2.json() 
print(data2)