print("Press 1 for Read , Press 2 for Write , Press 3 for Update ,press 4 for create")
operation=int(input("Enter What you want to perform :"))

if(operation==4):
    open("new.txt","x")

elif(operation==3):
    apply=open("new.txt","a")
    print(apply.write(input("enter message"))) 

elif(operation==2):
    apply=open("new.txt","w")
    print(apply.write(input("enter message"))) 

else:
    apply=open("new.txt","r")
    print(apply.read())
    