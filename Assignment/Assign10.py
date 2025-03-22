# Problem 1
# Write a python script to remove the last digit from a given nubmer.(for example, if user enters 2534 then your output should be 253)
'''
x = int(input("Enter a number:"))
x = x//10
print(x)
'''

# Problem 2
# Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output)
'''
x = int(input("Enter a number:"))
x = x%10
print(x)
'''

# Problem 3
# Write a python script to swap data of two variables.
'''
a = 10
b = 20
a = a^b # 30
b = a^b # 20
a = a^b # 10
print(a,b)
# a,b = b,a
'''

# Problem 4
# Write a python script which takes a three digit number from the user and displays only its first digit.
'''
x = int(input("Enter a three nubmer:"))
x = x//100
print("First digit is: ",x)
'''

# Problem 5
# Write a ptyhon script which takes a three digit number from the user and display its middle digit.
x = int(input("Enter a three nubmer:"))
x = x//10
x = x%10
print("Middle digit is: ",x)