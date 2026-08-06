# Dictionary

# A dictionary stores data as key: value pairs — like a real dictionary where you look up a word (key) to find its meaning (value)

# d={20:40,30:60,40:80,50:100}

# Where key works as index in the dictionary if you want to acess individual value from dictionary then you can use keys bcz indexing do not work in this .

# print(d[20]) #40
# print(d[40]) #80

# CRUD Operation

# Creating new key-value pair by vanilla python .

# d[60]=120

# print(d)

# Updating the value by vanilla python .
# d[20]=20

# print(d)

# Dictionary method


# d={20:40,30:60,40:80,50:100}


# For empty the dictionary
# d.clear()
# print(d)


# Getting the value 

# print(d.get(30))

# Getting a list having individual  tuples of each key and pair .

# print(d.items())
# print(d.keys())
# print(d.values())

# d.pop(20)
# d.popitem() # Remove last element .
# print(d)


# Return the value of the specific key. If the key does not exist , insert the key , with the specific value.

# print(d.setdefault(20,10000))

# d.update({30:50})

# Traversing in the dictionary 

# d={20:40,30:60,40:80,50:100}

# for i in d:
#     print(f"Key {i} : Values {d[i]}")

# Practice 1

# l1 = {"name1" : "Rohan" ,"course1":"B.Tech","year1":"3rd"}
# l2={"name2" : "Rohan" ,"course2":"B.Tech","year2":"3rd"}

# l1.update(l2)

# for i in l2:
#     l1[i]=l2[i]

# print(l1)



# Practice 2 
d={1:23,2:45,3:67,4:78}

sum=0
for i in d:
    sum+=d[i]
print(sum)    

# Practice 3 

# l1=["a","b","a","c","b","a"]
# d={}

# for i in range(0,len(l1)):
#     count=0
#     for j in range(0,len(l1)):
#         if(l1[i]==l1[j]):
#             count+=1
#     d.setdefault(l1[i],count)        
    
# print(d)