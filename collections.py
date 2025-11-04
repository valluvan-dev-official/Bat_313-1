
# Collections :

"""
    list
    tuple
    set
    dictionary

"""

# Sequence Data Type :

"""
List , Tuple
"""

# List :

"""
    - Lists are used to store multiple items in a single variable
    - List items are ordered
    - changeable
    - allow duplicates
    - changeable means :
        we can change,add and remove items in a list after it has been created   

    - list items can be any datatype.

"""

# list constructor : list()

"""
numbers = list((10,20,30,40,50))

print(numbers)
print(type(numbers))

"""

# Access List Items :
"""
    using indes=x to print the values

    using positive and negative index slicing 

    membership operator
"""

# Example :


"""
fruits = ["apple","orange","mango","banana","papaya"]

# print(fruits[-4:-1])

# Using membership Operator :

# print("apple" in fruits)


# Change List items:

# fruits[0] = "Tiger"

# fruits[0:3] = ["VAruun"]

# print(fruits)


# Insert List Items : insert(index,item)

fruits.insert(1,"ABCD")

print(fruits)


"""


# Add List Items :

"""
1. append() - add a single element to the end of the list
2. extend() - add elements of another iterable
"""

"""
# Append :

fruits = ["apple","orange","mango","banana"]

# fruits.append("papaya")

# Extend :

numbers = [1,2,3,4,5,6]

fruits.append(numbers)

print(fruits)

"""

# Remove List Items :

"""
1. remove
2. pop
3. del 
4. clear

"""

# remove() - Remove the first occurrence of a specified value

"""
a = [10,20,30,40,20,60]

print(a.remove(20))

print(a)

"""

# pop() - Remove and return an element at a specific index [default remove the last element]

"""
a = [10,20,30,40,50]

print(a.pop(1))

print(a)

"""

# clear() - removes all elements from the list
"""
a = [1,2,3,4]

a.clear()

print(a)

"""

# index(), count()


# sort() - 

"""
    - sort() case sensitive
    - resulting in all capital letters being sorted before lowercase letters

# a = [10,50,90,20,60,30,80,40]

a = ["orange","apple","papaya","cherry","mango","banana","Apple","Mango","Banana","Orange","Cherry"]

a.sort()
# a.sort(reverse=True)

print(a)

"""

# reverse() :

# copy() :

"""
a = [1,2,3,4]

b = a.copy()

print(b)

"""

# List joins :

"""
a = [1,2,3,4]
b = [5,6,7,8]

c = a + b

print(c)

"""

# Tuple() :

"""

    - used to Store multiple elements in a single variable
    - ordered
    - unchangeable
    - allow duplicates

"""

# constructor :

"""
a = tuple((1,2,3,4,5))

# a = (1,)

print(a)
print(type(a))

"""

# Update a tuple:

"""
a = (10,20,30,40,50)

x = list(a)

x[2] = 100

a = tuple(x)

print(a)

"""

# remove items in tuple :


# Unpack a tuple : using Asterick - *

"""
fruits = ("apple","orange","mango","banana")

a,*b,c =  fruits

print(a)
print(b)
print(c)

"""

# Set Data type :

"""
    - Used to store multiple items in a single variable
    - unordered
    - unchangeable
    - do not allow duplicates
    - do not have a defined order

    - Once set is created, you can't change its itms, but you can remove items and add new items

    - True and 1 are considered as a same value and are treated as a duplicats.
    - False and 0 are considered as a same value and are treated as a duplicates

    a = {20,102.45,"apple"}
"""

# a = {1,2,3,"varun","arun"}

"""
a = set((10,20,30,10,50))

print(a)

print(type(a))

"""

# Access set items :

"""
a = {"apple","orange","mango"}

for i in a:

    print(i)

"""

# Add new items : add()

"""
a = {1,2,3,4,5}

a.add("apple")

print(a)

"""

# update()

"""
x = {1,2,3,4}
y = {5,6,7,8}

x.update(y)

print(x)

"""


# Union :

"""
x = {1,2,3,4}
y = {5,6,7,8}

z = x.union(y)

print(z)

"""

# remove items :

"""
discard()
remove()
pop()
clear()

"""

# intersection()

# difference()


# Dictionary :

# mydict = {'name' : "Vimal","age":25,"Address":"Chennai",'name':"mathan"}

"""
    unordered collection of key-value pairs
    do not allow duplicates
"""

# print(mydict)

# print(type(mydict))


# cces Dict Values and Keys :


# mydict = {'name' : "Vimal","age":25,"Address":"Chennai"}


# print(mydict["name"])

"""
# get() :

print(mydict.get("Addressssssss"))

"""

# Keys() :

# print(mydict.keys())


# values() :

# print(mydict.values())


# items() :

# print(mydict.items())



# update() :

# mydict.update({'name':"Vijay"})

# print(mydict)



# mydict = {'name' : "Vimal","age":25,"Address":"Chennai"}



# Remove Dict items :


# print(mydict.pop('age'))

# popitem :

# mydict.popitem()

# clear()

# print(mydict)



#  ============= Nested Dictionary =================


"""
family = {
    "Member-1" : {"name":"varun","age":25},
    "Member-2" : {"name" : "Dharsha","age" : 28}
          } 

"""

"""
Member_1 = {"name":"varun","age":25}

Member_2 = {"name" : "Dharsha","age" : 28}


family = {
    "Member-1" : Member_1,
    "Member-2" : Member_1
}

"""
# print(family["Member-2"]["age"])


# Adding elements to the nested dictionary :


family = {
    "Member-1" : {"name":"varun","age":25},
    "Member-2" : {"name" : "Dharsha","age" : 28}
          } 


# family["Member-2"]["age"] = 30

# print(family)


# remove Elements from nested dictionary :


family["Member-2"].pop("name")

print(family)



























