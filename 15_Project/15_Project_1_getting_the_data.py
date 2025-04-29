import requests

# Wysyłanie zapytania GET do endpointu (lista stacji pomiarowych)
response = requests.get('https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll')

# Wyświetlenie odpowiedzi
if response.status_code == 200:  # response.status_code == 200 - UDALO SIE, == 400 - NIE UDALO SIE; jest bardzo duzo liczb oznaczajacych 
                                 # czy sie udalo, czy nie, dlaczego itp.
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")