# Zadani z ksiazki

# 1. Why are functions advantageous to have in your programs?
# Because they organize the code and prevent the entire code from crashing due to a single error

# 2. When does the code in a function execute: when the function is deﬁned or when the function is called?
# When the function is called

# 3. What statement creates a function?
# def function_name(parameters):
#    what_function_does

# 4. What is the difference between a function and a function call?
# A function is a code, calling a function causes it to run

# 5. How many global scopes are there in a Python program? How many local scopes?
# There's one global scope and the number of local scopes is less or the same as the number of functions

# 6. What happens to variables in a local scope when the function call returns?
# Variables are destroyed

# 7. What is a return value? Can a return value be part of an expression?
# Return value is a value returned by a function after the function is executed
# Return value can't be a part of expression but in function code there should be 
# the part of the code informing about the retur value, defining it

# 8. If a function does not have a return statement, what is the return value of a call to that function?
# None

# 9. How can you force a variable in a function to refer to the global variable?
# By adding "global" before variable
# e.g. global x

# 10. What is the data type of None?
# The None value is the only value of the NoneType data type
# None is when there is no return value of the function

# 11. What does the import areallyourpetsnamederic statement do?
# It imports some module

# If you had a function named bacon() in a module named spam, how would you call it after importing spam?
# bacon()

# How can you prevent a program from crashing when it gets an error?
# By try and except functions

# What goes in the try clause? What goes in the except clause?
# try code_that_is_executing_in_normal_case
# except code_that_is_executing_when_encounter_an_error