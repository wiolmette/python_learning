# Zadanie praktyczne z ksiazki - rozwiniecie z try i except

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

try:   # try musi stac przed ta linijka w ktorej moze pojawic sie blad (ValueError)
    number = int(input("Give a number "))

    while number != 1:
        number = collatz(number)
        
except ValueError: 
    print("This is not a number")