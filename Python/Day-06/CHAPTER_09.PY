# DATA STRUCTURE IN PYTHON 

# In built data structures are the data structures that are already defined in the python programming language. These data structures are used to store and organize data in a specific way. The built-in data structures in python are:
# 1. List
# 2. Tuple
# 3. Set    
# 4. Dictionary




# 1. list : list is a collection of items that are ordered and changeable(mutable). It allows duplicate members. Lists are written with square brackets.

# a=[24,26,28,30]
# print(a)


# print(type(a))  # <class 'list'>

# 1.Also you can  acess the elements of a list by using the index number bcz of its ordered nature. The index number starts from 0.

# print(a[0])
# print(a[-1])


# 2.Mutability of list: Lists are mutable, meaning that you can change, add, and remove items in a list after it has been created.

# Example of mutability of list:

# b=['moon',10045.23,True]
# print(f"Original list: {b}")

# b[2]=False

# print(f"Modified list: {b}")

# 3. list allow duplicate members: Lists can have items with the same value.

# b=['moon',10045.23,True,'moon']
# print(f"List with duplicate members: {b}")


# 4. Traversing a list: You can traverse through the list items by using a for loop.


# It can be done in two ways:

# 1 traversing on values of list:

# l1=[5,10,15,20,25,30]

# for i in l1:
#     print(i)

# 2. traversing on index of list:

# l1=[5,10,15,20,25,30]

# for i in range(len(l1)):
#     print(l1[i])


# list method : And if you don't know the methods of list then you can use the dir() function to get the list of all the methods of list.

print(dir(list))

# 1.append(): This method is used to add an item to the end of the list.

# l2=[22,33,44,55,66,77,88]

# l2.append(99)

# print(l2)


# Insert(): This method is used to add an item at a specific index in the list.

# l2.insert(3,100)
# print(l2)


# pop() : This method is used to remove an item from the list at a specific index. If no index is specified, it removes and returns the last item.

l2=[22,33,44,55,66,70,77,88,90,22]

# r1_item=l2.pop()
# print(r1_item)
# print(l2)




# r2_item=l2.pop(5)
# print(r2_item)
# print(l2)


# remove() : This method is used to remove the first occurrence of a specific item from the list. If the item is not found, it raises a ValueError.

# l2.remove(22)
# print(l2)

# clear() : This method is used to remove all items from the list, making it empty.

# print(l2.clear())


# sort() : This method is used to sort the items of the list in ascending order by default. You can also specify the reverse parameter to sort in descending order.

# l2.sort() # for ascending order
# print(l2)

# l2.sort(reverse=True) # for descending order
# print(l2)

# reverse() : This method is used to reverse the order of the items in the list.
# l2.reverse()
# print(l2)



# index() : This method is used to find the index of the first occurrence of a specific item in the list. If the item is not found, it raises a ValueError.

# print(l2.index(22))  # it will return the index of first occurrence of 22 in the list l2

# extend() : This method is used to add all the items from another iterable (like a list, tuple, or set) to the end of the list.

# l3=[100,200,300]

# l2.extend(l3)
# print(l2)  # it will add all the items of l3 to the end of l2

# count() : This method is used to count the number of occurrences of a specific item in the list.

# print(l2.count(22))  # it will return the number of occurrences of 22 in the list l2


# copy() : This method is used to create a shallow copy of the list. It returns a new list that contains the same elements as the original list.

l2_copy=l2.copy()
print(l2_copy)  # it will return a new list that contains the same elements as the original list l2

l2_copy.append(1000)
print(l2_copy)  # it will return a new list that contains the same elements as the original list l2 but with 1000 added to the end of the list

print(l2)  # it will return the original list l2 without any changes