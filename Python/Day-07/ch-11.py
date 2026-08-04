#  sets 

# A set automatically removes duplicates and has no guaranteed order. Great for checking membership and performing math-style set operations.

s={1,2,3,3,3,3,3,3,4,5}

print(s)
print(type(s))

# In the ram it stored as  the  hash value , so if we try to store duplicate value  it see it already hve that hash value so it exclued . 

print(hash(s))