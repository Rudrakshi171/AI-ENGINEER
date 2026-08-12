# File Handling : File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface


# File Modes
# r : Read only
# w : Write
# a : Append to end
# x : Create (if does not exist)
# Can perform using open ().

# For Creating new File.

# open("hello.txt","x")


# For writing the file 
# file=open("Birthday_Message.txt","w")

# data=input("Enter the birthday wish ")

# file.write(data)


# for opening the file

# file=open("Birthday_Message.txt",'r')
# print(file.read())

# append 
# file=open("Birthday_Message.txt",'a')
# print(file.write("Thanks for you lovely wishes"))

# or you can write this way also to escape from error .

with open("Birthday_Message.txt",'r') as err:
    print(err.read())