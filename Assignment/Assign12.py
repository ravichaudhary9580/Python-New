# Problem 1
#  Write a python script to check whether a given number is positive or non-positive?
'''
num = int(input("Enter a number: "))
if num>0:
    print("Positive")
else:
    print("Non-Positive")
'''

# Problem 2
# Write a python script to check whether a given number is divisble by 5 or not
'''
num = int(input("Enter a number: "))
if num % 5 == 0 and num>0:
    print("Divisble by 5")
else:
    print("Not-divisble by 5")
'''

# Problem 3
# Write a python script to check whether a given number is even or odd
'''
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
'''
    
# Problem 4
# Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a==b:
    print(a,"is equal",b)
elif a>b:
    print(a,"is greater")
else:
    print(b,"is greater")
'''

# Problem 5
# Write a python script to print two given words in dictionary order
'''
word1 = input("Enter a word: ")
word2 = input("Enter another word: ")
if word1>word2:
    print("Dictionary order is:")
    print(word2,word1)
else:
    print("Dictionary order is:")
    print(word1,word2)
'''