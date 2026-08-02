# Function
# A function is a reusable block of code with a name. Instead of writing the same logic 10 times, you write it once as a function and call it 10 times.

# There is two types of functions in Python:
# 1. Built-in functions   
# 2. User-defined functions 

# user-defined functions are created by the user to perform specific tasks. They are defined using the `def` keyword followed by the function name and parentheses.

# def winner():
#     print("Congratulations! You are the winner!")


# winner()  Calling the function to execute its code


# Pailindrome using function





def is_pailindrome(num):

    rev=0
    a=num
    while(num>0):

        rem=num%10
        rev=rev*10+rem
        num=num//10
    
    if(rev==a):
      print("The number is a palindrome")
    else:
      print("The number is not a palindrome")


is_pailindrome(121)
is_pailindrome(123)
is_pailindrome(12321)


# Parameters and Arguments
# parameters are variables that are defined in the function definition. They act as placeholders for the values that will be passed to the function when it is called. Arguments are the actual values that are passed to the function when it is called.

# Types of arguments:
# 1. Positional arguments : In this type of argument, the values are passed to the function in the same order as the parameters are defined. The first value is assigned to the first parameter, the second value to the second parameter, and so on.

def sum(a,b,c,d):
   return a+b+c+d

result=sum(1,2,3,4)
print(result)


# 2.Default arguments : In this type of argument, the parameters are assigned default values. If the function is called without passing any value for that parameter, the default value will be used. and if a value is passed, it will override the default value.

# And also if you want to use default arguments, you must define them after the non-default arguments. Otherwise, you will get a syntax error.


# def mul(a,b,c,d=8):
#    return a+b+c+d

# result=mul(1,2,3,4)
# print(result)

#This one will give an error because the default argument is not defined after the non-default arguments.
#  def sum(a,b,c=4,d):
#    return a+b+c+d

# result=sum(1,2,3,4)
# print(result)



# 3. Keyword arguments : In this type of argument, the values are passed to the function using the parameter names. This allows you to pass the values in any order, as long as you specify the parameter names.


def greet(name,age):
    print(f"Hello {name}, you are {age} years old.")

greet(age=25,name="John")  # Keyword arguments    


# Note: In this also if you want to use keyword arguments, you must define them after the non-keyword arguments. Otherwise, you will get a syntax error.