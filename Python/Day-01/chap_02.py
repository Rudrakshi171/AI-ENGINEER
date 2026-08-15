# Data types in python
"""
Every value in Python has a type that tells Python what kind of data it is and what you can do with it. You don't need to declare types — Python figures it out automatically.


"""
""" 
  
 The Main Data Types
 1. int :-  ( whole numbers: 1, 42, -7)
 2. float :- ( decimal numbers: 3.14, -0.001, 2.0)
 3. list

 4.bool :- ( True or False)
 5. complex :- ( Complex number : 1+2j, 3-4j) that's means of complex number is a combination of real and imaginary numbers.
 6. String :- ( A string is a sequence of characters enclosed in single or double quotes. For example, "Hello, World!" is a string.)

 7. Boolean :- ( A boolean is a data type that can have one of two values: True or False. It is often used in conditional statements and logical operations.)

 8. tuple
 9.Dictionary
 10.set
"""

# Checking the type of a variable: You can use the type() function to check the type of a variable.
# a1=123
# a2=2.342
# s3="bro"
# s4=1+3j

# print(type(a1))
# print(type(a2))
# print(type(s3))
# print(type(s4))

# Here is the representation of maximum no that python can handle 
# integer
# print(1e308)
# float
# print(1.7e308)


# Dynamic typing in python 
# while  declaring the variable in python we donot declare its type   bcz python interpreter is intelligent enough to understand it by its value.
# a=1234

# Dynamic binding in python

# while using a varible ,the variable can hold multiple values of both same or different data type. 
# a=234
# print(a)
# a="beautiful"
# print(a)
#  but in static binding the same variable can not redeclare as it type is already declare like in c,c++,java


# way of creating multiple variables
# a,b,c,d,e=12,45,78,89,45
# print(a,b,c,d,e)

# or

# a=c=f=g=r=678
# print(a,c,f,g,r)



# Keywords : These are some reserved words by the compiler and interpreter to understand the code.

# In python they are some 32 keywords.

#python  store input as string bcz it is universal format all data type can conert from this. 
first=int(input("Enter first number : "))
second=int(input("Enter second number : "))
sum=first+second
print(sum)


# literal are the raw value stored in the variable.