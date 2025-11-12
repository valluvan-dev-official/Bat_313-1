# Lambda with map(function,iterable) :

"""
    map - applies a function to each item in an iterable and returns an iterator
"""

# fruits = ["apple","orange","mango","banana"]

"""
numbers = [2,3,4,5]

square = list(map(lambda x : x ** 2,numbers))

print(square)

"""


# Lambda with Filter :

"""
filter is used to filter elements based on condition
"""

# Example:

"""
fruits = ["apple","orange","mango","banana"]


without_e = list(filter(lambda x : "e" not in x, fruits))


print(without_e)
"""


# reduce() :

"""
applies a function cumulatively to the elements in an iterable.
"""

"""
from functools import reduce


numbers = [1,2,3,4,5]

total = reduce(lambda x,y : x + y,numbers )

print(total)
"""

# sorted :

# sorted can use a lambda functions as a sorting key.
"""
fruits = [("Apple",50),("orange",30),("mango",40),("banana",25)]

sorted_ = sorted(fruits,key=lambda fruit : fruit[0])

print(sorted_)

"""

# Lambda with conditional  expression :

num = lambda a,b:"Greater than b" if a > b else "less than or equal to b"

print(num(20,90))