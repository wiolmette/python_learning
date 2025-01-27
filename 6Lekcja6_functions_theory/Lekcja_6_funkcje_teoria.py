# local and global scope

def spam(): 
    eggs = 99 
    bacon()             # mozna wywolac funkcje ktora jest zdefiniowana pozniej w kodzie
    print(eggs) 
 
def bacon():
    ham = 101
    eggs = 0 

spam()                  # wynik to 0 bo eggs z funkcji spam zniknelo w momencie wywolania tej funkcji
                        # kolejna wywolywana funkcja to bacon wiec eggs z bacon zostalo wywolane

def spam2(): 
    eggs2 = 99 
    bacon2()  
 
def bacon2():
    eggs2 = 0 
    print(eggs2)
 
spam2()

# globac variable can be read from the local scope (by a function)

def spam3(): 
    print(eggs3) 
eggs3 = 42 
spam3() 
print(eggs3)

# global statement 

def spam4(): 
    global eggs4             # variable eggs become global
    eggs4 = 'spam'           # there's no local variable eggs
                             # the line above define global variable eggs
 
eggs4 = 'global'             # variable eggs is defined second time
spam4()                      # spam function is called (with eggs4 variable = spam)
print(eggs4)                 # spam is printed 