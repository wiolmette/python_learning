# Zadania z ksiazki

# Zad. 1
# Boolean values are: True, False

# Zad. 2
# Three Boolean operators are: and, or, not

# Zad. 3 
# and
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False
# or
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False
# not
# not True -> False
# not False -> True

# Zad. 4
# (5 > 4) and (3 == 5) -> False
# not (5 > 4)  -> False
# (5 > 4) or (3 == 5) -> True
# not ((5 > 4) or (3 == 5)) -> False
# (True and True) and (True == False) -> False
# (not False) or (not True) -> True

# Zad. 5
# Comparison operators: ==, !=, >, <, >=, <= 

# Zad. 6
# equal to ==, assignment =

# Zad. 7
# Condition - logical operation, expressions that evaluate to True or False
# Condition is used e.g. in while loops

# Zad. 8
# Blocks differ in indentantion length 

# Zad. 9 Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 
# is stored in spam, and prints Greetings! if anything else is stored in spam.
import random
spam = random.randint(1,3)
if spam == 1:                # if a nie while bo gdy natrafi na np. while spam == 1 to bd nieskonczona petla!
    print("Hello")
if spam == 2:
    print("Howdy")
if spam == 3:
    print("Greetings")

# Zad. 10
# When the program is stuck in an infinite loop, press CTRL+C

# Zad. 11
# Break - stops the loop if the condition is true (before its natural termination)
# Continue - if the condition is true, the loop skips current iteration 
# and starts the loop from beginning

# Zad. 12
# range(10) - from 1 to 9 with interval 1
# range(0, 10) - from 0 to 9, with step 1
# range(0,10,1) - from 0 to 9, with step 1 (step = 1 is defined)

# Zad. 13
for i in range(1,11):
    print(i)
j = 1
while j < 11:
    print(j)
    j = j + 1

# Zad. 14
# spam.bacon()

# Zad. 15 extra
# round() - zaokragla
# skladnia: round(number, ndigits) ndigits - l. miejsc po przecinku
a = round(3.5464564,3)
print(a)
# abs() - zwraca wartosc bezwzgledna
# skladnia: abs(number)
b = abs(-10)
print(b)