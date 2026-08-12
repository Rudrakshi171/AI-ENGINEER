# Exception Handling

# Error  Vs Exception

# Error are something that is unfixable like syntaxerror , Indentation error , taberror.

# Exceptions are something that can be handleable (i.e yhat can be fixed or handle) like ZeroDivisionError , Typeerror, valueerror , filenotfounderror ) by using try,except,else,finally,raise.

# Syntaxerror example

# a="Do not fry my mind "bro" " 
# print(a)


# Indentation error

# if(True):
# print("Hello")

# Zero Division Error

# a=10
# b=int(input("Enter the value : "))  # 0
# print(a/b)


# Type error example
# a=25
# b="25"
# c=a+b
# print(c)

# Value error
# percentage=int(input("enter your percentage"))
# print(percentage)

# Here's how you can handle the error ,using keyword like try,except,finally,else,raise.
# Try: In this we write the block in which error can occured.
# Except : In this we write the block which will run if error occured in try block (Handle the exception).
# Error : In this we write the block which will run if error not occured.
# Finally : The code written inside this block will always run whether error occured or not .

a=int(input("Enter the value : "))
b=int(input("Enter the value : ")) 

try:
    print(a/b)

except Exception as err:
    print(f"Sorry an error occured as {err}")
else:
    print("No error occured")    


finally:
    name=input("Tell your name :- ")    
    print(f"Hello your name is {name}")


# raise : Used to manually throw your own Exception.

# age=int(input("Enter Your age : "))

# if(age>=18):
#     raise TypeError("You are not eligible to make licsence")



        