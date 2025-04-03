# Problem 1
# Write a python script to reverse a string word wise (for example- "mysirg education services" is a given string should be "services education Mysirg")
'''
l1 = input("Enter a string:").split(' ')
l1.reverse()
print(' '.join(l1))
'''


# Problem 2
# Write a python script to extract numbers from a given text and store all the numbers in a list.
'''
text = input("Enter numbers with comma:")
l1 =[]
for e in text.split(' '):
    try:
        l1.append(float(e))
    except:
        pass
print(l1)
'''

# Problem 3
# Write a  python script to check whether it is palindrome or not.
'''
s = input("Enter a string:")
length = len(s)
i = 0
x = len(s)
while x//2:
    if s[i] == s[length-i-1]:
        i+=1
    else:
        print("Not Palindrome")
        break
    x-=1
else:
    print("Palindrome")
'''
# s = input("Enter a string:")
# print("Palindrome" if s == s[::-1] else "Not Palindrome")

# Problem 4
# Write a python script to transform a given string to uppercase.
'''
print(input("Enter a string:").upper())
'''

# Problem 5
# Write a python script to find maximum length word in a given text.
'''
text = input("Enter the text:").split(' ')
max = -1
for x in text:
    if len(x) > max:
        max = len(x)
        value = x
print(max,value)
'''