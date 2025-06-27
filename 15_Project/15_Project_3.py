# Zadanie 1 – polacz sie z API i pobierz dane

import requests
import json

response = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll')  # endpoint zaczyna sie od http i trzeba go dac w apostrofy!!!
data = response.json() 
print(data)
print(data['Lista stacji pomiarowych']) 
print(len(data['Lista stacji pomiarowych']))

# Zadanie 2 - samodzielny wypis stacji)
print(type(data['Lista stacji pomiarowych']))
print("Numery i nazwy stacji: ")
lista_stacji = data['Lista stacji pomiarowych']
for i in range (0,10):
    print(lista_stacji[i]['Identyfikator stacji'], "-",  lista_stacji[i]['Nazwa stacji'], "(", lista_stacji[i]['Nazwa miasta'], ")")

# Zadanie 3 – Wyświetl sensory dla wybranej stacji
print(type(data['Lista stacji pomiarowych']))
lista_stacji = data['Lista stacji pomiarowych']
for i in range (0, len(data['Lista stacji pomiarowych'])):
    print(lista_stacji[i]['Identyfikator stacji'], "-",  lista_stacji[i]['Nazwa stacji'], "(", lista_stacji[i]['Nazwa miasta'], ")")

numer_stacji = input("Podaj numer stacji, ktorej stanowiska (sensory) chcesz wyswietlic ")
response1 = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/station/sensors/'+numer_stacji)
data1 = response1.json()
print(json.dumps(data1, indent=4, ensure_ascii=False))
print(data1['Lista stanowisk pomiarowych dla podanej stacji'])
print(data1['Lista stanowisk pomiarowych dla podanej stacji'][0])
print(data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Identyfikator stanowiska'])
print("-")
print(data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Wskaźnik - wzór'])
print(data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Identyfikator stanowiska'], "-", data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Wskaźnik - wzór'])
numer_stacji1 = data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Identyfikator stanowiska']
mierzony_parametr = data1['Lista stanowisk pomiarowych dla podanej stacji'][0]['Wskaźnik - wzór']
print(numer_stacji1, "-", mierzony_parametr)

print("Numery i nazwy sensorow:")
for i in range (0, len(data1['Lista stanowisk pomiarowych dla podanej stacji'])):
    print(data1['Lista stanowisk pomiarowych dla podanej stacji'][i]['Identyfikator stanowiska'], "-", data1['Lista stanowisk pomiarowych dla podanej stacji'][i]['Wskaźnik - wzór'])

# Zadanie 4 
response2 = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/data/getData/52?size=50')
data2 = response2.json()
print(data2)
print(len(data2['Lista danych pomiarowych']))
numer_sensora = input("Podaj numer sensora, ktorego wyniki chcesz wyswietlic ")

response3 = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/data/getData/'+numer_sensora+'?size=50')
data3 = response3.json()       
print(data3)
for element in data3['Lista danych pomiarowych']:
    print(element["Data"], "-", element["Wartość"], "µg/m³")
print(type(element))