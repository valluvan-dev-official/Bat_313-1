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



"""
class myclass(ABC):

    @abstractmethod
    def myfun(self):
        pass


class child(myclass):

    def myfun(self):

        print("Thank You")


p1 = child()

p1.myfun()

"""

# print("Wecome")
























#  Python Project :



class Library(ABC):


    @abstractmethod
    def add_book(self):
        pass

    @abstractmethod
    def view_book(self):
        pass

    @abstractmethod
    def issue_book(self):
        pass

    @abstractmethod
    def return_book(self):
        pass

    @abstractmethod
    def delete_book(self):
        pass



class College(Library):
    
    def __init__(self,x):
        
        self.storage = x

    def add_book(self):
        
        if self.storage == []:
            
            count = int(input("How many books do you want to add? "))
            
            for i in range(count):
                
                book_name = input("Enter Book Name : ")
                
                self.storage.append(book_name)
                
            print("Books Added Successfully..")
            
        else:
            
            book_name = input("Enter Book Name : ")
            
            self.storage.append(book_name)
            
            print("Book Added Sucessfully")
            

    def view_book(self):
        
        for sno,name in enumerate(self.storage,101):
            
            print(f"{sno} - {name}")

    def issue_book(self):
        
        issue_book = input("Enter the book name that you want? ")

        if issue_book in self.storage:
            
            self.storage.remove(issue_book)
            
            print("Book issued Successfully")
            
        else:
            
            print("Book is not Available..!")
        
    def return_book(self):
        
        return_book = input("Enter the book name you rturned : ")
        
        self.storage.append(return_book)
        

    def delete_book(self):
        
        delete_book = input("Which book do you want to delete? ")


        if delete_book in self.storage:
            
            self.storage.remove(delete_book)
            
            print("Book Removed Successfully")
            
        else:
            
            print("Book is Not At the Store")

store_books = []

obj = College(store_books)


while True:

    print("\nWelcome..!")

    print("\nChoose your Option : ")

    print("\n1. Add book")
    print("\n2. View book")
    print("\n3. Issue book")
    print("\n4. Return book")
    print("\n5. Delete book")
    print("\n6. Exit")
    
    
    option = int(input("\nEnter your Option as a Number : 1/2/3/4/5/6"))


    if option == 1:
        
        obj.add_book()
        
    elif option == 2:
        
        obj.view_book()
        
    elif option == 3:
        
        obj.issue_book()
        
    elif option == 4:
        
        obj.return_book()
        
    elif option == 5:
        
        obj.delete_book()
        
    else:
        
        break































