# Encapsulation :

"""

    - the idea of wrapping data and the methods that work on data with one unit

    - the wrapping concept  helps in controlling access to the data and provides a 
    way to protect the data from unintended interference or unauthorized access by 
    keeping it with in the boundaries of class.


    access specifiers or access modifiers :

    - public
    - private
    - protected

"""


# Public :

"""
class person:

    name = "bala"


    def salary(self):
        
        print("my salary is : ", 10000)


p1 = person()

print(p1.name)  # accessing public data member
p1.salary()     # accessing public member function



p2 = person()

print(p2.name)  # accessing public data member
p2.salary()     # accessing public member function

"""


# Private :

"""
    - accessible with in the class only, not outside the class "__" 

# Example :

class person:

    __name = "bala"

    
    def __salary(self):
        
        print("my salary is : ", 10000)
        
    
    def mfun(self):
        
        print("my funtion")
        self.__salary()
        print(self.__name)


p1 = person()

print(p1.name)  # accessing public data member
print("====================")
p1.mfun()   # accessing private member function  --> AttributeError

"""

# Protected :

"""
class person:

    name = "bala"

    
    def _salary(self):
        
        print("my salary is : ", 10000)
        
    
    def mfun(self):
        
        print("my funtion")
        self._salary()
        print(self.name)


class employee(person):

    def empfun(self):

        print("employee function")
        self._salary()
        print(self.name)




p1 = person()

# print(p1.name)  # accessing public data member
# p1.salary()   # accessing protected member function  --> AttributeError

p1.mfun()


p2 = employee()

p2.empfun()

"""


# Abstraction :

"""
    - The process of hiding complex implementation details and exposing only the necessary functionalities or interfaces to the user

    abstraction is used to hide the innerfunctionality of the function from the users.

    the users only interact with basic implementation of the function but inner working is hidden

    user is familiar with that "what function does" but they don't know "how it does"

    we need to import the abc module which provides the base for defining Abstract Class(ABC)

"""

from abc import ABC,abstractmethod



class myclass(ABC):

    @abstractmethod
    def myfun(self):
        pass


class child(myclass):

    def myfun(self):

        print("Thank You")


p1 = child()

p1.myfun()