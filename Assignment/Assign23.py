# Problem 1
# Write a python script to calculate factorial of a given number.
'''
num = int(input("Enter a number:"))
fact = 1
while num:
    fact *= num
    num -= 1
print("Factorial:", fact)
'''

# Problem 2
# Write a python script to count digits in a given number.
'''
num = int(input("Enter a number:"))
count = 0
while num:
    num //= 10
    count +=1
print("Digit count:", count)
'''

# Problem 3
# Write a python script to calculate sum of digits of a given number.
'''
num = int(input("Enter a number:"))
sum = 0
while num:
    sum = sum + num%10 
    num //= 10
print("Digit sum:", sum)
'''

# Problem 4
# Write a python script to print binary equivalent of a given decimal number. ( Do not use bin() method)
'''
num = int(input("Enter a number:"))
string = ''
while num:
    string += str(num%2)
    num //=2
string = string[::-1]
string = '0b' + string
print(string)
# print(int(string,2))
'''

# Problem 5
# Write a python script to print octal equivalent of a given decimal number. ( Do not use oct() method)
'''
num = int(input("Enter a number:"))
string = ''
while num:
    string += str(num%8)
    num //=8
string = string[::-1]
string = '0o' + string
print(string)
# print(int(string,8)) 
'''