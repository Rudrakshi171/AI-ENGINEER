# Strings in python

# In python specifically, strings are a sequence of unicode characters ( It is 16 bit characters ). 
  

# In python, string is a data type that is used to represent text. It is enclosed in either single quotes (' ') or double quotes (" "). Strings can be manipulated using various built-in methods and operators.


# And it can be defined in python using single quotes, double quotes, or triple quotes.

# triple quotes are used to define multi-line strings or docstrings.

# double quotes are used to define strings that contain single quotes, and single quotes are used to define strings that contain double quotes. 
 
greeting='hello,Rudrakshi hello'

# print(greeting);

# Here are some common string methods in Python:

# 1.len(): This method returns the length of a string.

# print(len(greeting))

# Accessing individual characters in a string can be done using indexing. In Python, strings are zero-indexed, meaning the first character has an index of 0.

# print(greeting[0])

# Accessing sub strings can be done using slicing. Slicing allows you to extract a portion of a string by specifying a start and end index.

# print(greeting[0:5])

# OR

# print(greeting[:5])

# print(greeting[6:])

# 2. lower(): This method returns a new string with all characters converted to lowercase.
# print(greeting.lower())

# print(greeting.upper())

# 3. count(): This method returns the number of occurrences of a substring in a string.It takes the substring as an argument and returns an integer representing the count of occurrences.
# print(greeting.count('hello'))

# print(greeting.count('l'))


# 4. find(): This method returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.It takes the substring as an argument and returns an integer representing the index of the first occurrence.

# print(greeting.find('hello'))

# print(greeting.find('l'))

# print(greeting.find('q'))


# print(greeting)
# 5. replace(): This method returns a new string with all occurrences of a substring replaced with another substring. It takes two arguments: the substring to be replaced and the replacement substring.
# new_greeting = greeting.replace('Rudrakshi','rudra')
# print(new_greeting)

# print(greeting)

# as we know that strings are immutable in python, so the original string remains unchanged after using the replace() method. If you want to update the original string, you need to assign the result of the replace() method back to the original variable.


wish='morning'

name='rudrakshi'

# Concatenation: You can concatenate strings using the + operator. This allows you to combine multiple strings into a single string.

message = wish + ", " + name + "!"
print(message.upper())

# or by using f-string formatting, which is a more concise and readable way to format strings in Python. It allows you to embed expressions inside string literals using curly braces {}.

message=f"{wish}, {name}!"
print(message)

# 6/ split(): This method splits a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). It takes an optional argument that specifies the delimiter to use for splitting.

message=(message.split(" "))

message="-".join(message)
print(message)
 # it will join the list of substrings into a single string, using the specified delimiter (in this case, a hyphen) between each substring.


college="    xyz college    "
print(college.strip())
# 7 strip(): This method removes leading and trailing whitespace characters from a string. It returns a new string with the whitespace removed. It does not modify the original string.

# way to know how many function can be used on string is by using dir() function. It returns a list of all the attributes and methods available for a given object.

# print(dir(message))


print(help(str)) # it will give you the documentation of string class and all the methods that can be used on string.


# for deleting any string you cAn use :
del str
print(str)