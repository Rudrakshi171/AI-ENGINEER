# Problem 1
# l1= [34,56,78,89,90]
# sum=0
# for i in l1:
#     sum+=i

# sum=sum/len(l1)
# print(sum)


# Problem 2 

# l2=[2,3,4,5,6,7,8,9]
# e1=[]
# for i in l2:
#     if i%2==0:
#         e1.append(i)

# print(e1)      
  
# Problem 3

# l2=[2,3,4,5,6,7,8,9]
# g_no=l2[0]
# indexxx=0

# for i in (0,7):
#     if(l2[i]>g_no):
#         g_no=l2[i]
#         indexxx=i

# print(f"Greatest element is {g_no} at index {indexxx}")        

# Problem 4
# l1=[3,4,5,6]
# l2=[7,28,2,9,12]

# l1.extend(l2)
# print(l1)
# l1.sort()
# print(l1)



# Problem 5

l1=[2,3,4,5,6,6,6,7,7,7]
l1=list(set(l1))
print(l1)

# problem 6 

t1=("Delhi","UttarPradesh","Uttarakhand","Rajasthan","Lucknow")
for i in t1:
    print(i)

# Problem 7

s1={2,3,4,5,6,7}
s2={5,6,7,8,9,10}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))