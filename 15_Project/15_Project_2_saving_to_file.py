import requests
import json

# Wysyłanie zapytania GET do endpointu (stacja w Walbrzychu)
response = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/aqindex/getIndex/109')

# Skladnia zapisywania pliku .json
# import json

# dane = {"miasto": "Wałbrzych", "jakosc_powietrza": "dobra"}

# with open("plik.json", "w", encoding="utf-8") as plik:
#     json.dump(dane, plik)

if response.status_code == 200:
    data = response.json()
    with open('E:/programowanie_git/python_learning/15_Project/stacje_pomiarowe.json', 'w') as file:
        json.dump(data, file)

else:
    print(f"Request failed with status code {response.status_code}")
