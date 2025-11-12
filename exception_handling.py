#  exception Handling :

"""
    - manage errors that might occur during program execution

    handles exceptions using try,except,else and finally


try:

    this block contains the code tha may raise an exception

except :

    handle the exception when an error occurs

else:

    executes only if th try blok runs successfully

finally :

    executes regardless of wether an exception occurs or not.

Types of errors in python :

    syntax error 
    Logical error
    runtime errors
    Type errors

"""

#  example :

"""
try:
    num = int(input("Enter your age : "))
    

except ValueError:
    print("Enter numeric values only")

else:

    print(num)

finally:

    print("Completed")

    """
# sin Multiple Exceptions :


try:

    num = int(input("Enter a number :"))

    division = 10 / num

except ValueError :

    print("Invalid Input!")

except ZeroDivisionError:

    print("Cannot divide by Zero!")

else:

    print(division)

finally:
    print("Finished")