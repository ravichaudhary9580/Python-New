# Problem 1
# Write a python script to print True if string 'my' is a member in a string entered by user. 
"""
a = 'my'
b = input("Enter a String: ")
if a in b :
    print("True")
else:
    print("Not Found") 
print('my' in input('Enter a string:'))
"""

# Problem 2
# Write a python script to input two strings from the user and display whether the two variables refered to same object or not. Print True or False.
'''
str1 = input("Enter a string: ")
str2 = input("Enter another string: ")
if id(str1) == id(str2):
    print("True")
    print(id(str1))
    print(id(str2))
else:
    print("False")
    print(id(str1))
    print(id(str2))
# print(input("Enter a string: ") is input("Enter another string: "))
'''

# Problem 3
# What will be the output of the python expression 5>10<5?   
# 5>10 and 10<5
# False and False
# False
'''
The expression 5 > 10 < 5 is a chained comparison in Python. However, it does not work as you might expect. Let's break it down:

Chained Comparisons: In Python, you can chain comparisons together, such as a < b < c. This is equivalent to (a < b) and (b < c).

Evaluation of 5 > 10 < 5:

The expression 5 > 10 evaluates to False.
The expression 10 < 5 also evaluates to False.
However, when you write 5 > 10 < 5, Python interprets it as (5 > 10) and (10 < 5). Both parts of this expression are False, so the entire expression evaluates to False.
'''

# Problem 4
# What will be the output of the python expression "Red" and "White" ?
# 'White'

# Problem 5
# What will be the output of the python expression True or False ?
# True