#  list is a mutable, ordered collection of elements.

flowers=['Rose','lilly','tulip','sunflower','jasmine','marigold']

#  print(len(flowers))
#  print(flowers)
#  print(flowers[0])
#  print(flowers[1])
#  print(flowers[2])
#  print(flowers[3])
#  print(flowers[4])
#  print(flowers[5])
# print(flowers[6])
# This will give an error because there is no index 6 in the list.

# print(flowers[:3])

# Here are some methods of list:
# 1. append() - adds an element to the end of the list.

# flowers.append('lotus')
# flowers[4]='hibiscus'
#  OR
# flowers.insert(5,'rosemary')
# print(flowers)

# flowers_2=['daisy','orchid','lavender','jasmine']

# flowers.insert(0,flowers_2)

# print(flowers)
# it will add the entire list flowers_2 as a single element at index 0 of the flowers list.
# But if you want to add the element of flowers_2 list to the flowers list, you can use the extend() method but you guys must be thinking that what is the difference between append() and extend() method. So, the difference is that append() method adds a single element to the end of the listand it will add this list but as a single element, while extend() method adds multiple elements to the end of the list.

# flowers.extend(flowers_2)
# print(flowers)

# Now , let's see how to remove an element from the list. There are several methods to remove an element from the list.
# 1. remove() - removes the first occurrence of the specified element.


list_1=[1,3,4,5,1,6]
list_1.remove(1)
print(list_1)

# 2. pop() - removes the element at the specified index and returns it. If no index is specified, it removes and returns the last element.

list_2=[1,3,4,5,1,6,6]
list_2.pop()
print(list_2)