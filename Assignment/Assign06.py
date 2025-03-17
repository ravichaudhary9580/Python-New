# Problem 1
# Write a python script to convert a number into str type. 
'''
x = str(45)
'''

# Problem 2
# Write a python script to print Unicode of the character 'm'. 
'''
print(ord('m'))
'''

# Problem 3
# Write a python script to print character representation of a given unicode 100.
'''
print(chr(100))
'''

# Problem 4
# Write a pyhton script to convert a str type data into an int type. Also describe when a str type value is not possible to convert into an int type. 
'''
x = '123' # Using str data
print(x,type(x))
x = int(x)
print(x,type(x))

x = '-123' # Using str data
print(x,type(x))
x = int(x)
print(x,type(x))
'''
# A str (string) type value cannot be converted into an int (integer) type if the string does not represent a valid integer. Here are some examples of when a string cannot be converted to an integer:
# '''
# 1. Non-numeric characters: If the string contains any characters that are not digits (0-9), it cannot be converted to an integer.
# '''
# s = "abc"
# int(s)  # This will raise a ValueError

# '''
# 2. Floating-point numbers: If the string represents a floating-point number (i.e., it contains a decimal point), it cannot be directly converted to an integer.
# '''
# s = "123.45"
# int(s)  # This will raise a ValueError

# '''
# 3. Empty string: An empty string cannot be converted to an integer.
# '''
# s = ""
# int(s)  # This will raise a ValueError

# '''
# 4. Whitespace: If the string contains only whitespace characters, it cannot be converted to an integer.
# '''
# s = "   "
# int(s)  # This will raise a ValueError

# '''
# 5. Special characters: If the string contains special characters (e.g., punctuation, symbols), it cannot be converted to an integer.
# '''
# s = "123!"
# int(s)  # This will raise a ValueError

# '''
# 6. Negative sign in the wrong place: If the string has a negative sign in the wrong place, it cannot be converted to an integer.
# '''
# s = "12-3"
# int(s)  # This will raise a ValueError

# Problem 5
x=874378 # True
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x=378   # True
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x='abc'   # True
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x=0 #False
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x=0.0 #False
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x=-0 #False
print(x,type(x))
x=bool(x)
print(x,type(x))
print("\n")

x=None #False
print(x,type(x))
x=bool(x)
print(x,type(x))

