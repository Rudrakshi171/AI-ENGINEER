# Conditional Statements: if, elif, else


# problem 1 :User se number lo. Check karo positive hai, negative hai, ya zero.

# i1=int(input("Enter a number: "))

# if i1>0:
#     print("Positive number")

# elif i1<0:
#     print("Negative number")

# else:
#     print("Zero")

    
# problem 2 :User se age lo. Print karo


# age=int(input("Enter your age :"))
# if age>0 and age<13:
#     print("You are a child.")
# elif age>=13 and age<20:
#     print("You are a teenager.")
# elif age>=20 and age<60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# problem 3 : User se marks lo (0-100). Grade print karo:

# marks=int(input("Enter your marks (0-100): "))
# if(marks>90 and marks<=100):
#     print("A")

# elif(marks>80 and marks<=89):
#     print("B")    


# elif(marks>70 and marks<=79):
#     print("C")

# elif(marks>60 and marks<=69):
#     print("D")  


# else:
#     print("F")



# problem 4 :User se 3 numbers lo. Sabse bada number print karo — max() use mat karo!

# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# num3=int(input("Enter Third number : "))

# if(num1>num2 and num1>num3):
#     print(f"{num1} is the largest number.")


# elif num2>num1 and num2>num3:
#     print(f"{num2} is the largest number")


# else:
#     print(f"{num3} is the largest number")


#  problem 5 : User se year lo. Check karo leap year hai ya nahi.

# year=int(input("Enter the Year:"))

# if(year%4==0 and (year%400==0 or year%100!=0)):
#     print(f"{year} is a leap year")


# else:
#     print(f"{year} is not leap year")



# Problem 6 : if -else example 
# 1. Find the min of 3 given number
# 2.Menu driven program


# 1. Find the min of 3 given number
# a=int(input("Enter first number"))
# b=int(input("Enter Second number"))
# c=int(input("Enter Third number"))

# if(a>b and a>c):
#     print(f"{a} is greator")
# elif(b>a and b>c):
#     print(f"{b} is greator")    
# else:
#     print(f"{c} is greator")    



# 2. Menu Driven operation

# num1=int(input("Enter the first number : "))
# num2=int(input("Enter the second number : "))

# op=input("Choose the operation you want to perform between (+,-,*,/,**) : ")

# if(op=='+'):
#     print(f"The sum of a and b is {num1+num2}.")
# elif(op=='-'):
#     print(f"The Difference of a and b is {num1-num2}.")
# elif(op=='*'):
#     print(f"The multiplication of a and b is {num1*num2}.")
# elif(op=='/'):
#     print(f"The division of a and b is {num1//num2}.")

# elif(op=='**'):
#     print(f"The power of a and b is {num1**num2}.")

# else:
#     print("You have choosen wrong operation")
