# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

# salary=int(input("Enter your Salary(in lakhs) : "))
# hra=0.10*salary
# da=0.05*salary
# pf=0.03*salary
# if(salary>=20):
#     tax=salary*0.30
    
# elif(salary<=10 or salary>20):
#      tax=salary*0.20
     

# elif(salary<=5 or salary>10):
#      tax=salary*0.10
     
# else:
#       tax=salary
              

# total_deduction=hra+da+pf+tax
# salary=salary-total_deduction
# print(f"Your salary is {salary}")

# Problem 2 :Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
# a1=int(input("Enter the angle 1 : "))
# a2=int(input("Enter the angle 2 : "))
# a3=int(input("Enter the angle 3 : "))


# a=a1+a2+a3
# if(a==180 and a1>0 and a2>0 and a3>0):
#     print("It can form a Triangle")
# else:
#     print("It can not form a triangle")    


# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

# c_p=int(input("Enter the cost price :  "))
# s_p=int(input("Enter the selling price :  "))

# if(s_p>c_p):
#     print("It is profit")
# else:
#     print("It is los" \
#     "s")    


# Problem 4: Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit


# op=int(input("Choose the operation (1 for cm to ft ),(2 for km to miles),(3 for USD to INR ),(4 for Exit)"))
# val=int(input("Enter the value :"))


# if(op==1):
    
#     print(f"Conversion of {val} from cm to ft is {val/30.48} ")
# elif(op==2):
#     print(f"Conversion of {val} from km to miles is {val/1.609} ")
# elif(op==3):
#     print(f"Conversion of {val} from usd to inr is {val*95.45} ")    
# elif(op==4):
#     print("exiting....")  
# else:
#     print("You have choosen wrong operation ")      
    

# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

# first=0
# second=1
# print(first,second, end=" ")
# for i in range(0,8):
#     a3=first+second
#     first=second
#     second=a3
#     print(a3,end=" " )


# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# num=int(input("Enter the number you want to find factorial :  "))
# fact=1
# for i in range(num,0,-1):
#     fact*=i
# print(f"Factorial of {num} is {fact}")    


# Problem 7 - Reverse a given integer number.
# Example:

# Input:

# 76542
# Output:

# 24567

# num=int(input("Enter the number you want to reverse  :  "))
# temp=num
# a=0
# while(num>0):
#     rem=num%10
#     a=a*10+rem
#     num=num//10
# print(f"Reverse of {temp} is {a}")
   


# Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. 
# Example 1:

# Input:

# 30
# Output:

# 276

# num=int(input("Enter the number : "))
# sum=0
# for i in range(1,num):
#     if(i%5==0):
#         continue
#     else:

#         if(sum<300):
#             sum+=i
#         else:
#             break    
    
# print(sum)


# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

# sum=0
# item=0
# while(True):
#     num=int(input("Enter the number : "))
    
#     if(num==0):
#         break
#     else:
#         sum+=num
#         item+=1

# av=sum//item  
# print(av)  

# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

# for i in range(1000,3000):
#     n=i
#     flag=True
#     while(n>0):
#         temp=n%10
#         if(temp%2!=0):
#             flag=False
#             break

#         n=n//10

#     if flag:
#         print(i,end=" ")    


# Problem 12:Write a program to print whether a given number is a prime number or not.

# num=int(input("Enter the number : "))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count+=1

# if(count==2):
#     print(f"{num} is prime")  
# else:
#     print(" Not Prime ")      


# Problem 13:Print  the Armstrong numbers in a given number.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

# import math

# num=int(input("Enter the number :  "))
# o_no=num
# cube=0
# while(num>0):
#     rem=num%10
#     cube=cube+math.pow(rem,3)
#     num=num//10
# if(cube==o_no):
#     print(f"{o_no} is armstrong ")
# else:
#     print(f"{o_no} is not armstrong")    


