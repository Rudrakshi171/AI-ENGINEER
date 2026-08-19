# while loop

# The while loop keeps running as long as a condition is True. You use it when you don't know how many times you'll need to repeat

# Problem 1

# Separate each digit of a number and print on a new line without using string conversion

# a=int(input("Enter the number"))

# while(a>0):
#     rem=a%10
#     print(rem)
#     a=a//10


# Problem 2

# Accept a number and print its reverse.

# reverse_num=0
# a=int(input("Enter the number"))

# original_num=a

# while(a>0):
#     rem=a%10
#     reverse_num=reverse_num*10+rem
#     a=a//10
    

# print(reverse_num)  


# Problem 3 

# keep accepting numbers from users till he/she enters a 0 then find the average .


# sum=0
# item=0
# while(True):
       
#        num=int(input("Enter the number :"))
#        if(num>0):
#         sum+=num
#         item+=1
#        else:
#            break
# av=sum//item
# print(av)


# Problem 4 
# The current population of a town is 10000.the population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years .


# year=(int(input("Enter the current year ")))
# current_population=10000
# for i in range(year-10,year):
#     print(f"In the {i} population is {current_population} ")
#     current_population=(current_population/1.10)
    


# Problem 5 
# sequence term 
# 1/1! + 2/2! +3/3! + ....

# num=int(input("Enter the number till you want to print the sum"))
# sum=0
# fact=1
# for  i in range(1,num+1):
#     fact=fact*i
#     sum+=i/fact
# print(f'The sum is {sum}')    



# Nested loops
# r=int(input("Enter the number of rows : "))
# for i in range(0,r):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()    
         

# r=int(input("Enter the number of rows : "))
# for i in range(0,r):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()    


# r=int(input("Enter the number of rows : "))
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(j,end="") 
#     for k in range(i-1,0,-1):
#         print(k,end="")    
#     print()  
  

# lower=int(input("Enter the lower limit : "))
# higher=int(input("Enter the higher limit : "))
# sum=0
# for i in range(lower,higher+1):
#     sum=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             sum+=1
#     if(sum==2):
#         print(i)            
