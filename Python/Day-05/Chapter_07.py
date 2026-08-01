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

reverse_num=0
a=int(input("Enter the number"))

original_num=a

while(a>0):
    rem=a%10
    reverse_num=reverse_num*10+rem
    a=a//10
    

print(reverse_num)  