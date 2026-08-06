#  sets 

# A set automatically removes duplicates and has no guaranteed order. Great for checking membership and performing math-style set operations.

# s={1,2,3,3,3,3,3,3,4,5}

# print(s)
# print(type(s))

# In the ram it stored as  the  hash value , so if we try to store duplicate value  it see it already hve that hash value so it exclued . 

# print(hash(s))

# s1={23,45,89,90}
# s1.add(59)
# s1.discard(23)
# s1.pop()

# print(s1)


s1={23,45,89,90}

s2={34,90,66,123}

# difference operation

# print(s1.difference(s2))
# print(s2-s1) # can write difference of sets by this way also


# difference update operation

# s2-=s1
# print(s2)

# Intersection operation

# print(s1.intersection(s2))

# intersection update operation

# s2&=s1
# print(s2)

# subset operation 

s3={90,60}

# print(s3.issubset(s2))

# or 

# print(s3<=s2)

# superset operation

# print(s2<=s3)

# symmetric difference: it return all the unique value between the set .

print(s2^s3)


# symmetric difference update

s2^=s3
print(s2)

# union set

print(s1.union(s2))

