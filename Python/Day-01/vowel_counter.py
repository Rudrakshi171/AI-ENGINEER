text=input("enter a string:")      

text=text.lower()

count=0

for i in text:
    if i in 'aeiou':
        count+=1



print("number of vowels in the string is:",count)