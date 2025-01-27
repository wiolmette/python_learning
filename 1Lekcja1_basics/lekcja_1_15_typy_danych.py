# integer (int) - l. całkowita
int1 = 5
print(int)
int2 = int1 - 10
print(int2)     # int moze byc ujemna

# float - l. zmiennoprzecinkowa
float1 = 1.5
float2 = int1 - float1
print(float2)
float3 = float1 - int1   # float może być ujemna
print(float3)
float4 = 3.46747483838292992
print(float4)   # nie ma limitu liczb po przecinku

# string (str) - łańcuch znaków
str = "lalala"  # str trzeba dawać w cudzysłów
print(str)

# bool - wartość logiczna: true, false
a = 15
bool_czy_wieksza_niz_10 = a > 10
print(bool_czy_wieksza_niz_10)
b = 10
c = 20
bool2 = b < c
print(bool2)
# dodatkowe funkcje bool:
print(bool(1))      # True, bo 1 jest prawdą
print(bool(0))      # False, bo 0 jest fałszem
print(bool([]))     # False, bo lista jest pusta
print(bool([1, 2])) # True, bo lista zawiera elementy

#list (lista) - przechowuje różne typy danych, ZMIENNA
# to co w liście w nawiasach kwadratowych, oddzielane przecinkiem
lista = [1, 3.5, ["Hejka", 3, 5.67388], bool2]
print(lista)

#tuple (krotki) - podobne do list ale NIEZMIENNE
# to co w krotce w nawiasach okrągłych, oddzielane przecinkiem
krotka = (1, 2.5, [3.343434, "Wiola"], bool2)
print(krotka)

# dictionary (dict) - słownik, służy do przechowywania danych klucz-wartość
pusty_slownik = {}
wiek_osob = { "Adam": 25, "Maria": 30, "Piotr": 22}
print(wiek_osob)
print(wiek_osob["Adam"])
print("Wiek Marii to", wiek_osob["Maria"]) # miedzy string a wartoscia trzeba dac przecinek

wiek_osob["Ewa"] = 15   # dodanie nowego elementu
print(wiek_osob)

wiek_osob["Adam"] = 26   # modyfikacja wartości elementu
print(wiek_osob)

del wiek_osob["Piotr"]  # usunięcie elementu
print(wiek_osob)

print("Klucze:", wiek_osob.keys())   # Klucze: dict_keys
print("Wartości:", wiek_osob.values())  # Wartości: dict_values
print("Pary klucz-wartość:", wiek_osob.items())  # Pary klucz-wartość: dict_items

imiona_osob = { "Osoba1": "Adam", "Osoba2": "Arek" }
print(imiona_osob)
imiona_osob["Osoba2"] = "Arkadiusz"
del imiona_osob["Osoba1"]
print(imiona_osob.values())

# operacje na różnych typach danych
# string
imieX = "Wiola"
powitanie = "Hej " + imieX + "" # jakaś dziwna składnia z "+"
print(powitanie)
print(imieX)
pozegnanie = "Nara " + imieX + ""   # tylko 1 cudzysłów na początku
print(pozegnanie)

print(imieX*3)  # powtórzenie

# list
lista = [1, 2, 3]
print(lista)
lista2 = [4, 5]
print(lista2)
lista3 = lista + lista2     # didawanie list
print(lista3)

lista.append(3.5)   # dodawanie elementu do listy
print(lista)

print(lista[1:3])   # slicing - wycinanie z listy

# konwersja typów danych
liczba = "8"
liczba_int = int(liczba)  # konwersja z str na int
print(liczba_int + 1)  # 9

liczba_float = float(liczba_int)  # konwersja na float
print(liczba_float + 1.5)  # 9.5

# nie nalezy nadpisywac funkcji pythona, np nie pisac "float = 5.0" tylko "float1 = 5.0"