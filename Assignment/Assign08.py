# Problem 1
# Write a python script to take your name as input from the user and then print it. 
'''
name = input("Enter your name:")
print("\033[32m", name, "\033[0m")
'''

# Problem 2
# Write a python script to take input two numbers from the user, then calculate their sum and display the result.
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Sum is:", a+b)
'''

# Problem 3
# Write a python script which takes the radius from the user and display area of the circle.
'''
from math import pi
radius = float(input("Enter the radius of Circle:"))
print("Area of Circle is:", pi*radius*radius, "Unit\u00B2")
'''

# Problem 4
# Write a python script to calculate square of a number. Number is entered by the user.
'''
x = float(input("Enter a number:"))
print("Square of", x, "is", x*x)
'''

# Problem 5
# Write a python script which takes a character from the user and display its unicode.
'''
char = input("Enter a Character:")
print("Unicode of", char, "is", ord(char))
'''

print(0x00B2, bin(0x00B2), oct(0x00B2), hex(0x00B2), chr(0x00B2))