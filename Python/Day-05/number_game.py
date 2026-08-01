import random
a=random.randint(1,100)

tries=0
b=int(input("Guess the number between 1-100 "))
tries+=1
while(True):
    if(b>a):
        print("Too High!")
        tries+=1
        b=int(input("Guess the number between 1-100 "))
    elif(b<a):
        print("Too Low")
        tries+=1
        b=int(input("Guess the number between 1-100 "))



else: 
        print(f"You are Correct and you take {tries} try")   

