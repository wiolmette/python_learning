# Zadania z ksiazki

# Zad. 1
# operators: *, -, /, +
# values: 'hello', -88.8, 5

# Zad. 2
# variable - spam, string - "spam" (spam - mielonka)
# (variable nie oznacza ze zmienna ma konkretna fumkcje,  
# tylko ze mozna nadac jej wartosc, np. spam = 2, spam = "Kwiat" itd.)

# Zad. 3
# 3 data types: integer - l. calkowita, string - ciag znakow, 
# dictionary - slownik (klucz + wartosc)

# Zad. 4
# experessions -  consist of values (such as 2) and operators (such as +),
# and they can always evaluate (that is, reduce) down to a single value.
# e.g. 2+2 -> can be reduced to 4

# Zad. 5 ?
# Expressions consists of values and operatrs, 
# Statements define the value of variables?
# e.g. spam = 5 <- statement
# 2*x <- expression 

# Zad. 6 ?
# bacon will be still equal to 20
# the result of the code will be: 21
bacon = 20
print(bacon + 1)

# Zad. 7 
# 'spam' + 'spamspam' = 'spamspamspam'
x = 'spam' + 'spamspam'
print(x)
# (stringi mozna zapisywac w pojedynczych i podwojnych " !!!)
# 'spam' * 3 = 'spamspamspam'
y = 'spam' * 3
print(y)

# Zad. 8 ?
# Names of variables can't be numbers?

# Zad. 9 ?
# integer -> int
# floating-point number -> float
# string -> string?

# Zad. 10
# 'I have eaten" + 99 + 'burritos'
# This expression cause error because it contains different kinds of 
# variables that can't be summed
# Possible resulotiun to this problem: change the integer 99 to string '99'
z = 'I have eaten' + ' 99' + ' burritos'
print(z)

# Extra zad. 11
# interactive shell - wiersz polecenia / terminal, np. powershell, Python
# power shell - rozbudowany terminal Windowsa (w cmd trzeba wpisac powershell)
# Python built-in Functions - oficjalna dokumentacja Pythona
# len() - funkcja zwracajaca dlugosc obiektu, w przypadku tekstu liczbe znakow
tekst = "Hello"
a = len(tekst)
print(a)
# round(liczba, n)  - zaokragla liczbe do n-tego miejsca po przecinku
b = round (5.1223822378438, 5)
print(b)