"""
 Each character in a string is stored with its own Unicode number. That's why strings use more memory than integers.which are stored as 4 bytes. The Unicode number for each character is stored in a sequence of bytes, which can take up more memory than a single integer value.
"""

a="hello ladies and Gentleman" 

# And if you want to know the Unicode number of a character in a string, you can use the ord() function. The ord() function takes a single character as an argument and returns its Unicode code point (an integer representing the character).
# every character in a string has a position, which is called an index. The first character in a string has an index of 0, the second character has an index of 1, and so on. You can use the index to access individual characters in a string.

# And index can be negative or positive. A negative index counts from the end of the string, with -1 being the last character, -2 being the second-to-last character, and so on.

# A positive index counts from the beginning of the string, with 0 being the first character, 1 being the second character, and so on.


print(ord(a[3]))

print(ord(a[4]))

print(ord(a[5]))

print(a[25],a[-1])

# slicing is a way to extract a portion of a string.

#  Syntax : string [start:end:step]
#  start: the index from where you wanna start slicing.
# end point: the index where you wanna end slicing. (the character at this index is not included in the slice)
# step: the number of characters to skip between each character in the slice. (default is 1, which means no characters are skipped)

print(a[6:26])

print(a[::3])

print(a[-1::-3])

print(a[-1:-6:-1])



# Type Conversion : Type conversion is the process of converting a value from one data type to another. In Python, you can use built-in functions to convert between different data types.

# 1. int(): The int() function converts a value to an integer. If the value is a string, it must represent a valid integer (e.g., "42" or "-7"). If the value is a float, it will be truncated (not rounded) to the nearest whole number.

a="-45"

b=(int(a))


print(a)
print(type(a))


print(b)
print(type(b))


print(int(True))
print(int(False))

# You can convert string if it holds valid integer.
# You can convert float to int .


# float(): The float() function converts a value to a floating-point number. If the value is a string, it must represent a valid float (e.g., "3.14" or "-0.5"). If the value is an integer, it will be converted to a float.

d="4.6743"

d=float(d)
print(d)
print(type(d))


e="34"
e=float(e)
print(e)
print(type(e))

# string(): The str() function converts a value to a string. This can be useful for concatenating different data types or for displaying values in a human-readable format.It work for all data types.

a=23
b=4567.312
c=True
d=345+5j

a=str(a)
b=str(b)
c=str(c)        
d=str(d)

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# bool() : the bool() function converts a value to a boolean (True or False). In Python, the following values are considered "falsy" and will be converted to False: None, False, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), empty sequences (e.g., "", (), []), and empty mappings (e.g., {}). All other values are considered "truthy" and will be converted to True.

print(bool(None))
print(bool(False))
print(bool(0))  
print(bool(0.0))
print(bool(0j))
print(bool([]))
print(bool(()))
print(bool({}))


# truthy values
print(bool(1))
print(bool(-1))
print(bool("hello"))
print(bool(45454))