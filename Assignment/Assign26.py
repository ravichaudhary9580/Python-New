# Problem 1
# Write a python script to check if a given string has only alphabets in it.
'''
string = input("Enter a string:")
print(string.isalpha())
'''

# Problem 2
# Write a python script to check if a given character is present in a given string or not.
'''
print('False' if input("Enter a string:").find(input("Enter a character:")) < 0 else 'True')
'''

# Problem 3
# Write a python script to count vowels in a given string.
'''
count = 0
for x in input("Enter a string:"):
    if x in 'aeiouAEIOU':
        count+=1
print(count)
'''

# Problem 4
# Write a python script to count words in a given string.
'''
l1=input("Enter a string:").split(' ')
count=0
for e in l1:
    if e != '':
        count+=1
print("Words:",count)
print(l1)
'''

# Problem 5
# Write a python script to reverse a string.
'''
print(input("Enter a string:")[::-1])
'''