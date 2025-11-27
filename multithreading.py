# Multi Threading :

"""
    Multithreading is a powerful concept in programming that allows you to run multiple threads concurrently.

    When you want to execute multiple tasks concurrently or simultaneously you can use threads.

"""

import threading
import time


# Key components in Threading :

"""
    Thread
    start()
    run()
    join()

    is_alive()
    current_thread()
"""

# Using Multiple threads :

import threading
import time

"""
def print_numbers():

    for i in range(1,6):
        
        print(f"Number : {i}")

        time.sleep(1)


def print_letters():

    for i in "Apple":

        print(f"Letter : {i}")

        time.sleep(1.5)



t1 = threading.Thread(target=print_numbers)
t1.start()


t2 = threading.Thread(target=print_letters)
t2.start()

t2.join()

print("Thank you BTREE")

"""


# Using thread in class :


class Myclass(threading.Thread):

    def drive(self):

        print("I'm drive a car")

        time.sleep(2)

    def run(self):

        time.sleep(2)

        print("Thread is running")

        self.drive()



t1 = Myclass()
t1.start()

print("Welcome")

# t1.drive()

print("Class thread is completed")


