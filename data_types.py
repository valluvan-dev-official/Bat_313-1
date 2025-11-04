# Data Types :

"""

    1. Numeric datatype
    2. Text Datatype
    3. Boolean Datatype
    4. Sequence Datatype
    5. Set Datatype
    6. Mapping Datatype
    7. None Type

"""

# Numeric Data type :

"""
    1. int - Integer
    2. float - float
    3. complex  - complex

"""

# Int  - int()

    # Unlimited Length 
    # Positive , negative or Zero

# a = 43
# print(type(a))


# Float : - float()

"""
    represents Real numbers with decimal point - 43.45
    unlimited Length
    Positive,Negative or Zero
    Scientific Numers are float - 3e4    
"""

# Complex : - commplex()

"""
3 + 4j

    real + Imaginary Values
    j - imaginary Unit

"""

# a = 3 + 4j


# print(a)
# print(type(a))



# ---------------------------------------------

"""
a = complex(23)

print(a)

print(type(a))

"""


# Text Data Type :

"varun" 'varun234' "345"

# str : string :- str()

"""
name = 'Vasanth'

print(name)

print(type(name))

"""

# Sequence Data Type :

"""
    List - list()

    Tuple - tuple()

    range()

"""

# List :

"""
fruits = ["apple","orange","mango","banana"]

print(fruits)
print(type(fruits))
"""

# Tuple :

"""
fruits = ("apple","orange","mango","banana")

print(fruits)
print(type(fruits))

"""

# Range - range() :

"""
r = range(1,5)

print(list(r))

print(type(r))

"""


# Mapping Data Type :


# dict() - Dictionary :


"""
x = {"name" : "varun", "age" : [30,30]}

print(x)
print(type(x))

"""

# Set Data Types :

# set()

"""
age = {20,40,80,50,70,20}

print(age)

"""


# Boolean DAta type :

# bool()


# a = True

# print(a)

# print(type(a))


# None Type :


"""
name = None 


print(name)

print(type(name))

"""

# Type Casting : explicit Convertion

"""
a = 50.234

b = int(a)

print(b)

"""

# Type Convertion : implicit convertion



"""

num = 2.14

a = 25

c = num * a
 
print(c)
print(type(c))

"""

# String :

"""
    - Stings are arrays 

  11 10 9 8 7 6 5 4 3 2 1  -

    h e l l o _ w o r l d

    0 1 2 3 4 5 6 7 8 9 10 +
"""

"""
a = "hello_world"

b = "welcome"

"""

# print(a[-1])

# String Slicing :a[start : end :step]

# print(a[0:4])

# print(a[-5:],b[0:5])

# print(a[0:11])

# print(b[0 : : 2])

# print(b[::-1]) - reverse a string



# -----------------------

"""
# Slice Between Two Words :

a = "DataScienceRocks"

# Task 2:

# a = "Computer" -> Cmue

# TAsk 3 :

# a = "Visualization" -> f-2 , L-2

# Task -3 :

# x = "Development" - eop --> 1 5 6

# Task 4 :

z = "XMachineYLearningZ"

"""
# z = "XMachineYLearningZ"

# print(z[1:17])


# String Modifications :

"""

    lower()

    upper()

    strip() - Remove White Space

    replace(old,new)

    split()
"""

# a = "Hello World"

# print(a.lower())

# print(a.upper())

# print(a)

# print(a.strip())


# print(a.replace(" ","_"))

# print(a)


# ===========  String Concatenation ============

"""
    we cannot combine strings & numbers

"""

# a = "Hello"

# b = "World"

# print(a + " " +b)



# ============= Format Strings : =============

# format() :

"""
 The format method takes unlimited number of arguments. are placed in respeective placeholders

"""

# salary = 35000

# name = "varun"

# age = 25


# msg = "hi i'm {2} and my salary is {0} and my age is {1}"

# print(msg.format(salary,age,name))


# f-String :


# msg = f"hi i'm {name} and my salary is {salary} and my age is {age}"

# print(msg)


# Escape Character :

"""

\'
\"
\n
\r
\t
\b

"""

# msg = "Welcome to Hello \"world\" "

# print(msg)














