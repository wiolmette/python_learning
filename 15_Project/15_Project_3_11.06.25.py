# Zadanie 1 – połącz się z API i pobierz dane

import requests
import json

response = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll')  # endpoint zaczyna sie od http i trzeba go dac w apostrofy!!!
data = response.json() 
print(data)
print(len(data))  # zle liczy, nie liczy liczby stacji