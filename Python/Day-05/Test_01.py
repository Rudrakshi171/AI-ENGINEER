# Problem 1

# name=input("Enter Your Name : ")
# age=int(input("Enter your age :"))
# height=float(input("Enter your height :"))
# print(f" Name: {name}, Age: {age}, Height: {height}")


# Problem 2



# characters=0
# sentence=input("enter a sentence : ")
# for i in range(len(sentence)):
#     if sentence[i].isalpha():
#         characters+=1

# print(f"Total number of characters in the sentence is : {characters}")
# print(f" Sentence in upper case : {sentence.upper()}")
# print(f" First character: {sentence[0]}, Last character: {sentence[-1]}")


# Problem 3


# for i in range(1,51):
#     sum=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             sum+=1

#     if(sum==2):
#         print(f"{i} is a prime number")


# Problem 4
   

num=int(input("Enter a number : "))
sum=0
while(num>0):
    rem=num%10
    sum+=rem
    num=num//10

print(f"Sum of digits: {sum}")