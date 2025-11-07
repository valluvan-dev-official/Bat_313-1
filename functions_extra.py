# Function returns multiple Values :



"""
def calc(a,b):

    add = a + b

    sub = a - b

    mul = a * b

    div = a / b

    return add,sub,mul,div



# print(calc(10,20))


a,b,c,d = calc(20,10)

print("Addition ",a)
print("Suptraction ",b)
print("Multiplication ",c)
print("Division ",d)

"""

# Scope of Variables :

"""
    - a variable scope specifies the region where we can access a variable.

    There are Three types of scope :

        1. Global Scope
        2. Local Scope
        3. Non Local Scope 


Global Scope :


"""

# Example for local scope :


"""
def myfun():

    num = 34

    print("Number is ",num)


# myfun()

print(num)

"""


# Global Scope :


"""
num = 40

def myfun():

    print(num)


# myfun()

print(num)

"""

# Non Local Scope :


"""
def Outer_function():

    name = "Abishek"

    def innerfunction():

        print(name)

    innerfunction()


Outer_function()

"""

# Lambda Function :

"""
    a lambda function is a small anonymus function.
    it can take any number of arguments, but can only have one expression
    it is used to define small functions


syntax :

    lambda arguments : expression

    lambda : keyword to define a lambda function.
    arguments : variables that are passed to the function.
    expression : a single expression that is evaluated and returned by the lambda function.

"""

# x = lambda a,b : (a + b) * 2 + a + b


# print(x(10,20))


# Example :

"""
marks = [95, 30, 76, 45, 88, 50]


result = lambda mark : "Pass" if mark >= 50 else "Fail"

for mark in marks:

    print(f"Mark : {mark} -> Result {result(mark)}")

"""

# Banking Interest Calculation :

savings_account = 5
fixed_deposit = 8


accounts = [
    ("Savings", 10000), # Account_type, amt
    ("Fixed", 50000),
    ("Savings", 15000),
    ("Fixed", 30000)
]

# Interest Calculation :

interest = lambda account_type,amt : amt * 0.08 if account_type == "Fixed" else amt * 0.05

for acc in accounts:

    print(f"{acc[0]} Account ${acc[1]} -> Interest Earned ${interest(acc[0],acc[1]):.2f}")






