# Problem 1 

# def greet(name):
#     print(f" Hello {name} ")


# greet("Rudrakshi")


# Problem 2

# def add(a,b):
#     return a+b

# sum=add(b=23,a=12)
# print(sum)

# Problem 3

# def is_even(num):
#     if(num%2==0):
#         print("True")
#     else:
#         print("False")

# is_even(9)
        

# Problem 4

# def square(num):
#     return num*num

# result=square(5)
# print(result)

# Problem 5

# def max_of_two(a,b):
#     if(a>b):
#         return a
#     else:
#         return b


# max=max_of_two(12,23)
# print(max)    
    
# Problem 6

# def count_vowels(string):
#     count=0
#     for i in range(len(string)):
#         if(string[i] in 'aeiouAEIOU'):
#             count+=1
#     return count

# print(count_vowels("Hello, World!"))

# Problem 7

# def reverse_string(string):
#     rev=""
#     for i in range(len(string)-1,-1,-1):
#         rev=rev+string[i]
#     print(rev)    

# reverse_string(" palak ")

# Problem 8

# def pailindrome(num):
#     original_num=num
#     reverse_num=0

#     while(num>0):
#         rem=num%10
#         reverse_num=reverse_num*10+rem
#         num=num//10

#     if(original_num==reverse_num):
#         print("The number is a palindrome")
#     else:   
#         print("The number is not a palindrome")    


# pailindrome(121)
# pailindrome(123)        



# pronblem 9


# def factorial(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num*factorial(num-1)


# print(factorial(5))    




