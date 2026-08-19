# import random
# a=random.randint(1,100)

# tries=0
# b=int(input("Guess the number between 1-100 "))
# tries+=1
# while(True):
#     if(b>a):
#         print("Too High!")
#         tries+=1
#         b=int(input("Guess the number between 1-100 "))
#     elif(b<a):
#         print("Too Low")
#         tries+=1
#         b=int(input("Guess the number between 1-100 "))



# else: 
#         print(f"You are Correct and you take {tries} try")   


#  Or 
import random
num=random.randint(1,200)
attempt=0

while(True):
    guess_num=int(input("Number is between 1 and 200. Start guessing! "))
    attempt+=1
    if(num==guess_num):
        print(f"You guess the correct number i.e {guess_num}")
        
        break
    elif(num>guess_num):
        print(f" Think above this number i.e {guess_num}") 
    
          

    elif(num<guess_num):
        print(f" Think below this number i.e {guess_num} ") 
        
           


print(f"In {attempt} attempt")