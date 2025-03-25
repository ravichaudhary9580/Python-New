# Problem 1
# Write a python script to print each character of a string with its corresponding Unicode.
'''
for e in 'ravi':
    print(e, ord(e))
'''

# Problem 2
# Write a python script to print only vowels of the given string.
'''
string = input("Enter a string:")
for e in string:
    for v in 'aeiou':
        if v == e:
            print(e)
'''

# Problem 3
# Write a python script to count occurrence of spaces in a given string.
'''
string = input("Enter a string:")
count = 0
for e in string:
    if e == ' ':
        count+=1
print("Space count:",count)
'''

# Problem 4
# Write a python script to print unique digits of a given integer.
'''
num = input("Enter a integer:")
for d in '0123456789':
    count = 0
    for e in num:
        if d == e:
            count += 1
    if count == 1:
        print(d)
'''

# Problem 5
# Write a python script to count number of digits in a given number.
# Using for when data type is str that is an iterator
'''
num = input("Enter a integer:")
count = 0
for e in num:
    count += 1
print("Digit count:", count)
# OR
# print(num.__len__())
'''

# Using while when data type is int
'''
num = int(input("Enter a integer:"))
count = 0
while num:
    num = num//10
    count += 1
print("Digit count:", count)
'''
