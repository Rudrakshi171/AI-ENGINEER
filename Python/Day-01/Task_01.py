# Q1 :- Print the given strings as per stated format.
# Given strings: "Data" "Science" "Mentorship" "Program" "By" "CampusX"
# Output: Data-Science-Mentorship-Program-started-By-CampusX



# print("Data","Science","Mentorship","Program","by","Campux",sep="-")


# Q2 Q2:- Write a program that will convert celsius value to fahrenheit.

# fahrenheit=int(input("enter the value of fahrenheit :"))

# celcius=(fahrenheit-32)*5/9

# print(celcius)

# Q3  Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

# a=int(input("Enter the  value of a :"))
# b=int(input("Enter the  value of b:"))

# c=a
# a=b
# b=c

# print(f'The value of a is {a} and The value of b is {b} after swapping')

# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

# import math
# c1=int(input("Enter the  value of c1 :"))
# d1=int(input("enter the value of d1 :"))

# c2=int(input("Enter the  value of c2 :"))
# d2=int(input("Enter the value of d2 :"))


# d=math.sqrt(c2-c1)**2 + (d2-d1)**2
# print(f"\nThe Euclidean distance between the points is: {d:.4f}")


# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

# principle=int(input("Enter the value of principle : "))
# rate=int(input("Enter the value of rate :"))
# time=int(input("Enter the value of time :"))
# si=(principle*rate*time)/100
# print(f"S.I is {si}")


# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

total_head=int(input("Enter the total heads : "))
total_legs=int(input("Enter the total legs : "))


Dogs=total_legs/4
chicken=total_legs%4

print(f"Total dogs are {Dogs}  and chicken are {chicken}")