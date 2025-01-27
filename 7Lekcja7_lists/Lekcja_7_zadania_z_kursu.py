# Zadania z listami

# Zad. 1 Filmy
# Utwórz listę swoich ulubionych filmów. Dodaj do niej dwa nowe tytuły, usuń jeden stary i wyświetl całą listę w konsoli.
ulubione_filmy = ["Titanic", "Skazani_na_Shawshank", "Substancja"]
ulubione_filmy.append("Madmax")         # Dodaje tylko 1 element (na koniec listy) - czy da sie dodac naraz wiecej?
ulubione_filmy.append("Bruce Wszechmogacy")
ulubione_filmy.remove("Skazani_na_Shawshank")
print(ulubione_filmy)

# Zad. 2 Dni tygodnia
# Stwórz listę zawierającą nazwy dni tygodnia.
# Wyświetl trzeci dzień tygodnia.
# Zmień nazwę drugiego dnia na "wtorek_zapnij_rozporek".
# Dodaj "chillera" na koniec listy.

dni_tygodnia = ["poniedziałekm", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
print(dni_tygodnia[2]) # 3ci element listy jest indeksowany 2, bo 1szy to 0!!!
dni_tygodnia[1] = "wtorej_zapnij_rozporek"
print(dni_tygodnia[1])
dni_tygodnia.append("chillera")
print(dni_tygodnia)

# Zad. 3 Temperatury
# Masz listę temperatur w stopniach Celsjusza z różnych dni tygodnia. 
# Twoim zadaniem jest przekonwertować te temperatury na stopnie Fahrenheita, 
# a następnie wyfiltrować i wyświetlić tylko te, które przekraczają 
# 75 stopni Fahrenheita. W trakcie tego zadania użyj funkcji konwersja.

temperatury_c = [20, 22, 19, 15, 25, 30, 18]
a = temperatury_c[0]*1.8+32
b = temperatury_c[1]*1.8+32
c = temperatury_c[2]*1.8+32
temperatury_f = [a, b, c]
print(temperatury_f)

temperatury_f_lista = []
for temperatura in temperatury_c:
    temperatura_f = temperatura*1.8+32
    if temperatura_f > 75:
        temperatury_f_lista.append(temperatura_f)   # tak zrobic liste!!!
print(temperatury_f_lista)


