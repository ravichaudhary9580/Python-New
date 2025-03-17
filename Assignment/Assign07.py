# Problem 1
# Write a python script to print any number and its binary equivalent.
'''
x=234
print(x,"Binary :",bin(x))
'''

# Problem 2
# Write a python script to store binary number 1100101 in a variable and print it in decimal format.
'''
x = 0b1100101
print(x,bin(x))
'''

# Problem 3
'''
x = 0x2F
print(x, oct(x))
'''

# Problem 4
# Write a python script to store an octal number 125 in a Variable and print it in binary formate.
'''
x = 0o125
print(x, bin(x))
'''

# Problem 5
# Write a pyhton script to add two numbers 25(in octal) and 39(in hexadecimal) and display the result in binary formate.
x = 0o25
y = 0x39

print(x,"Octal:",oct(x))
print(y,"Hexadecimal:",hex(y))

print("Sum of", x, "+", y, "is", x+y, "Binary:", bin(x+y))
