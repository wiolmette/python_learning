# for
print('My name is') 
for i in range(5): 
    print('Jimmy Five Times (' + str(i) + ')')      # zamiana stringa na int: str(i) 
                                                    # konieczne bo nie mozna dodawac int do stringa 
# opcja bez zamiany int na stringa, ale wtedy on jest obok a nie miedzy stringami (nawiasami)
print('My name is') 
for j in range(5): 
    print('Jimmy Five Times', j)

# while
j = 0
while j < 6:
    print('Jimmy Five Times (' + str(j) + ')')
    j = j + 1
# range(start, stop, step), step moze byc ujemny aby schodzic z liczbami w dol
for k in range(10, 20, 2):
    print(k)
for l in range(5,-3,-1):
    print(l)