#  Tuples : It is a collection of ordered and immutable elements. Tuples are defined by enclosing the elements in parentheses ().

# Note :  A tuple is exactly like a list, except you cannot change it once created. Use tuples for data that should stay constant — like days of the week, coordinates, or config values.


# t1=(23,'root',3.14,True)
# print(t1)
# print(type(t1))


# note : YOu can convert a list to a tuple using the tuple() function.

# l1=[23,45,67,89]
# t1=tuple(l1)
# print(t1)
# print(type(t1))


# as we  know that tules are immutable , so it only have two methods count() and index().
 

# l3=(34,67,89,34,111,222,333,111,285,111)

# print(l3.count(111))
# print(l3.index(111))


# There is one another way also to create the tuple by separating value by commas 

t=234,444,6677
print(type(t))