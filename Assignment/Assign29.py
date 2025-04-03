# Problem 1
# Write a python script to create a tuple from a given list.
'''
l1 = input("Enter some values:").split(' ')
print(l1,type(l1))
print(tuple(l1),type(tuple(l1)))
'''

# Problem 2
# Write a python script to reverse a tuple.
'''
t1 = tuple(input("Enter some values:").split(' '))
print(t1)
t1 = t1[::-1]
print(t1)
'''

# Problem 3
# Write a python script to create a list of tuples from a given list of strings, where each tuple is a collection of strings begin with the same character.
'''
l1 = [e for e in input("Enter some values:").split(' ') if e]# list of strings
l1 = sorted(l1)
firstchar = l1[0][0]
l2 = [] # temp list
l3 = [] # list of tuples
for e in l1:
    if e.startswith(firstchar):
        l2.append(e)
        continue
    else:
        firstchar = e[0]
    l3.append(tuple(l2))
    l2 = []
    l2.append(e)
l3.append(tuple(l2))
print(l1)
del l2
print(l3)
'''

# Problem 4
# Write a python script to create a list of tuples, where each tuple is a pair of elements, first element is uppercase character and second element is its unicode.
'''
s1 = input("Enter some text:")
l1 = []
for e in s1:
    temp = []
    temp.append(e.upper())
    temp.append(ord(e))
    l1.append(tuple(temp))
print(l1)
'''


# Problem 5
# Write a python script to find the sum of all odd numbers stored in a tuple.
'''
t1 = tuple([int(e) for e in input("Enter some values:").split(' ')])
print(t1)
sum = 0
for e in t1:
    if e%2 == 1:
        sum += e
print(sum)
'''