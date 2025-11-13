# File Handling :

"""
Two Types of files :

    1. Text   file -  t(default)
    2. Binary file -  b 

    
# Opening a file :

f = open("filename","Mode")

Modes in File Handling :

    1. r - read
    2. a - append
    3. w - write
    4. x - create


    read:
     
       default value, opens a file for reading. Raises an error if the file does not exist.

    append :

        Opens a file for appending, creates the file if it does not exist.

    write:

        Opens a file for ariting, creates the ffile if does not exist.

    create :

        creates the spefied file, raises an error if the file exists.

reading files: 

   read()
   readline()
   readlines()


"""

f = open("file_handling/sample.txt","r")

# print(f.read(10))
# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())