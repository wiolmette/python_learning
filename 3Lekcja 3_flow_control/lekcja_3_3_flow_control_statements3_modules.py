# random.randint() - losowy integer; random - modul, randint - funckja
import random 
for i in range(5): 
    print(random.randint(1, 10))
# break zamiast exit
while True: 
    print('Type exit to exit.') 
    response = input() 
    if response == 'exit': 
        break                                   # break przerywa petle ale nie program
    print('You typed ' + response + '.')
# sys.exit() - konczy program
import sys 
while True: 
    print('Type exit to exit.') 
    response = input() 
    if response == 'exit': 
        sys.exit()                              # exit przerywa program dlatego nic po tej petli juz nie zostanie zrobione
    print('You typed ' + response + '.')