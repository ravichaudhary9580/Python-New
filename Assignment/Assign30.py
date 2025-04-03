# Problem 1
# Write a python script to print all distinct element of a list. Use set to solve the problem.
'''
l1 = input("Enter elements seprated by comma:").split(',')
print(set(l1))
'''

# Problem 2
# Create two sets from a given set of numbers to separate even and odd numbers. 
'''
s1 = set(int(e) for e in input("Enter elements seprated by comma:").split(','))
print(s1)
even = set()
odd = set()
for e in s1:
    if e%2:
        odd.add(e)
    else:
        even.add(e) 
print(even)
print(odd)
'''

# Problem 3
# Given a set of five player names. Write a Python script to form all possible pairs of players that is selecting two players at a time.
'''
name = set(input("Enter 5 players name:").split(' '))
pairs = []
for e in name:
    for x in name:
        if e!=x:
            value = e,x
            value = sorted(value)
            if value not in pairs:
                pairs.append(tuple(value))
print(set(pairs))
print(len(set(pairs)))
'''

# Problem 4
# You have a list of names of candidates, some of them are wearing black hat, some of them are wearing red shoes and some of them are wearing both. Now you have given a list of names of candidates wearing black hat. There is another list of names of candidates wearing red shoes. Write a python script to find out the names of the candidates wearing black hat and red shoes.
'''
students = input("Enter names:").split(' ')
black_hat = set(input("Enter names with black hat:").split(' '))
red_shoes = set(input("Enter names with red shoes:").split(' '))
print("Students wearing black hat and red shoes",black_hat.intersection(red_shoes))
'''


# Problem 5
# Write a python script to create a set of tuples, where each tuple has two elements representing dice upper face number. Take a number N from the user and generate all possible tuples, in such a way that tuple elements sums to N.
'''
'''
N = int(input("Enter a number:"))
possible = set()
for d1 in range(1,7):
    for d2 in range(1,7):
        if d1+d2 == N:
            value = d1,d2
            possible.add(value)
print("All the possible pairs with sum",N,':',possible)    