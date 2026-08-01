# Loops


#  range():It contains three parameter start from where it start,stop till it will work ,and step how much step you have to take to reach to nextrespectively.
# i.e : range(start,stop,step) 


# For loop 

# for j in range(0,101,20):
#     print(j)


# simple problem of printing table 

# n=int(input("Enter number which table you want to print : "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# range function in string
# domain="ai enginerr"

# for i in domain:
#     print(i)

# for i in range(len(domain)):
#     if domain[i]==" ":
#         continue
#     print(domain[i])


# for i in range(len(domain)):
#     if domain[i]=="    ":
#         break
#     print(domain[i])

# else:
#     print("no break was encountered")    


# Problem 1

# n=int(input("enter how many time you want to wish :  "))

# for i in range(1,n+1):
#     print("Hello")


# Problem 2 

# num=int(input("Enter till you want to print : "))

# for i in range(1,num+1):
#     print(i)


# Problem 3


# num=int(input("Enter from  you want to print : "))

# for i in range(num,0,-1):
#     print(i)

# Problem 4 

# sum=0
# num=int(input("Enter till you want to print sum  : "))

# for i in range(1,num+1):
#     sum=sum+num

# print(sum)    


# Problem 5

# num=int(input("Enter  you want to print factors : "))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)



# Problem 6

# sum=0
# num=int(input("Enter the number you wanna check : "))
# for i in range(1,num):
#     if(num%i==0):
#         sum+=i

# if(sum==num):
#     print(f"{num} is a perfect number")    
# else:
#     print(f"{num} is not a perfect number")    
# 
# 
# problem 7     


# sum=0
# num=int(input("Enter the number you wanna check : "))
# for i in range(1,num+1):
#     if(num%i==0):
#         if(i==1 or i==num):
#             sum+=1
#         else:
#             break    
# if(sum==2):
#     print(f"{num} is a prime number")            
# else:
#    print(f"{num} is not a prime number")     

#          or 

# sum=0
# num=int(input("Enter the number you wanna check : "))
# for i in range(1,num+1):
#     if(num%i==0):
#         sum+=1 
# if(sum==2):
#     print(f"{num} is a prime number")            
# else:
#    print(f"{num} is not a prime number") 


# Problem 8

# reversed_str=""
# original_str=input( "Enter the string you wanna Reversed: ")
# for i in range(len(original_str)-1,-1,-1):
#     reversed_str+=original_str[i]


# print(reversed_str)

# problem 9

# reversed_str=""
# original_str=input( "Enter the string you wanna Reversed: ")
# for i in range(len(original_str)-1,-1,-1):
#     reversed_str+=original_str[i]


# if(original_str==reversed_str):
#     print(f"{original_str} is a pailindrome")


# else:
#     print(f"{original_str} is not a pailindrome")    


# problem 10
string = input("Enter a string: ")

letters = 0
digits = 0
symbols = 0

for char in string:
    if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
        letters += 1
    elif 48 <= ord(char) <= 57:
        digits += 1
    else:
        symbols += 1

print(f"Letters={letters}, Digits={digits}, Symbols={symbols}")