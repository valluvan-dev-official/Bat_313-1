# Decorators :

"""
    Decorators are a powerful and flexible feature that allows you to modify or extend the behaviour of a functions or classes without changing their actual code.

definition :

    a decorator is a high-order function that allows a function or class as an argument,add some funtionality or modifies it and returns a new funtion or class.

    Decorators are commonly used for logging and timing functions, authentication and authorization caching modifying function behaviour dynamically based on condition.
"""

# Example:

"""
def Outerfunction(func):

    def Innerfunction():
        
        print("Welcome to BTREE")

        func()

        print("Thank You for Comming")

    return Innerfunction

@Outerfunction
def myfun():

    print("Btree Python Training Course")


myfun()


# result = Outerfunction(myfun)

# print(result())

"""



def Upperstring(func): # function as a argument

    def process():

        data = func()

        return data.upper()


    return process  # function return another function



def Split(x):

    def process():

        data = x()

        return data.split()

    return process 


@Split
@Upperstring     # function decorate with decorators
def new():

    return "hello all welcome to Btree"



print(new())