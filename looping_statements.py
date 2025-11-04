# Looping  Statements :

"""
    1. For Loop
    2. While Loop
"""

# For Loop :

"""

    over a sequnce of items(list,tuple,dict,set,string)

    [1,2,3,4,5]


syntax :

    for variable in iterable :

        block of code
"""

"""
fruits = ["Apple","Orange","Mango","Banana"]


for i in fruits: # apple orange mango banana

    print(i) # a , o , m , b

"""

# Example 2 :

# Using BreaK & Continue :

"""
Break - Exit the loop immediately
continue - skip the current iteration

"""


"""
numbers = [1,2,3,4,5]

for i in numbers: # 1 2 3 4 5

    if i == 3: # 1 == 3
        # break
        continue

    print(i + 10) # 11 12 14 15

"""

# Else in For Loop :


# Else block execute if the loop completes.

"""
numbers = [1,2,3,4,5]

for i in numbers:

    if i == 4:
        continue

    print(i)

else:

    print("Loop finished successfully.")

"""

# Nested Loops :

# a loop inside another loop is called a nested loop.

"""
a = ["apple","Orange","Mango"]

b = [10,20,30]


for fruit in a: # apple

    for number in b : # 10 20

        print(f"{fruit}  -  {number}")

"""

# Range in For Loop : range(start,end,step)


"""
for i in range(1,15,2):

    if i == 4:

        continue

    print(i)

"""


# While Loop :

"""
    Do something Repeatedly until the condition is true
    The Number of iterations is not predefined
    The Loop executes untill the condtion becomes False

Syntax :

    while condtion:

            block of code
"""


"""
i = 0 # 1 2 3 4 5

while i < 5 : 

    print(i) # 0 1 2 3 4

    i += 1 

"""

# Else in while loop :

"""
i = 0 
while i < 5 : 

    if i == 3:
        break

    print(i) 

    i += 1

else:

    print("loop finished")

"""

# break and continue :


i = 0 

while i < 5 : 

    i += 1
    
    if i == 3:
        # break
        continue

    print(i) # 0 1 2
