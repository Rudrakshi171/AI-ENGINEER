# Loops


#  range():It contains three parameter start from where it start,stop till it will work ,and step how much step you have to take to reach to nextrespectively.
# i.e : range(start,stop,step) 


# For loop 

# for j in range(0,101,20):
#     print(j)


# simple problem of printing table 

n=int(input("Enter number which table you want to print : "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


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

sum=0
num=int(input("Enter till you want to print sum  : "))

for i in range(1,num+1):
    sum=sum+num

print(sum)    


