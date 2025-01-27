# Zadanie praktyczne z ksiazki

number = int(input("Give a number "))

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1

print(collatz(number))