# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

def fibonacci_series(limit):
    a, b = 0, 1
    while b <= limit:
        print(b, end=" ")
        temp = a + b
        a = b
        b = temp

fibonacci_series(50)