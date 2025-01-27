# flow control statements:
# if + condition:
    # clause
# condition to np. a + b == 4
# if clause to np. print("suma a i b = 4")
# else:
    # else clause
# elif - kolejny warunek ktory jest sprawdzany
# tylko gdy poprzednie sa false
# elif + condition:
    # elif clause
# np. 
name = 'Wiola'
age = 10
if name == 'Alice': 
    print('Hi, Alice.') 
elif age < 12: 
    print('You are not Alice, kiddo.')
# przykald z if, elif i else
x = 8
if x < 5:
    print("x jest mniejsze niż 5")
elif x < 10:
    print("x jest mniejsze niż 10, ale większe lub równe 5")
else:
    print("x jest większe lub równe 10")
# zagniezdzone if - zwracac uwage na polozenie if i else 
# i wciecia (if i else tego samego zdania musza byc na
# tym samym wcieciu)
y = 7
if y > 4:
    print("y jest wieksze od 4")
    if y > 6:
        print("y jest wieksze od 6")
    else:
        print("y jest mniejsze lub rowne od 6")
else: 
    print("y jest mniejsze od 4")
# elifow mozna dac wiele, kazdy sprawdzany jesli poprzednie 
# warunki beda false; w przypadku true - na tym sie konczy 
# kolejnosc jest wazna!!!
name2 = 'Carol' 
age2 = 150 
if name2 == 'Alice': 
    print('Hi, Alice.') 
elif age2 < 12: 
    print('You are not Alice, kiddo.') 
elif age2 > 2000: 
    print('Unlike you, Alice is not an undead, immortal vampire.') 
elif age2 > 100: 
    print('You are not Alice, grannie.')