# Problem 1
# Write a python script to print each character of a string with its corresponding Unicode.
'''
for e in 'ravi':
    print(e, ord(e))
'''

# Problem 2
# Write a python script to print only vowels of the given string.
'''
for e in input("Enter a string:"):
    if e in 'aeiouAEIOU':
        print(e)
        
for e in input("Enter a string:"):
    for v in 'aeiouAEIOU':
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
# print("Unique digits:",set(str(int(input("Enter a number:")))))
'''
num = int(input("Enter a integer:"))
num = str(num)
i = 0
for e in num:
    if num.index(e) == i:
        print(e)
    i += 1
'''
# num = int(input("Enter a integer:"))
# s = ''
# for e in str(num):
#     if e not in s:
#         s+=e
# print(s)
 
# Problem 5
# Write a python script to count number of digits in a given number.
# Using for when data type is str that is an iterator
'''
num = int(input("Enter a integer:"))
count = 0
for e in str(num):
    count += 1
print("Digit count:", count)

# OR
# print(len(num))
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
