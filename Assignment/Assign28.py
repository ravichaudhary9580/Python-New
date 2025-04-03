# Problem 1
# Write a python script to remove all non int values from a list.
'''
l1 = input("Enter text:").split(' ')
print(l1)
l2 = []
for x in l1: 
    try:
        l2.append(int(x))
    except:
        pass
l1 = l2
del l2
print(l1)
'''

# Problem 2
# Write a python script to print distinct elements along with their frequencies of occurrences in the list.
'''
l1 = input("Enter text:").split(' ')
l1 = sorted(l1,reverse=True)
print(l1)
value = l1[0]
print("Frequency of", l1[0], 'is:', l1.count(l1[0]))
for e in l1:
    if value != e:
        occ = l1.count(e)
        print("Frequency of", e, 'is:', occ)
    value = e
print(len(l1))
'''

# Problem 3
# Write a python script to sort a list of strings
'''
l1 = input("Enter text:").split(' ')
print(l1)
l1 = sorted(l1)
print(l1)
'''

# Problem 4
# Write a python script to find first repeated string in a list of strings
'''
l1 = input("Enter text:").split(' ')
print(l1)
for x in l1:
    if l1.count(x)>=2:
        print("First REPEATED string is",x)
        break
'''

# Problem 5
# Write a python script to count strings which ends at character 's' in a list of strings.
'''
l1 = input("Enter text:").split(' ')
print(l1)
count = 0
for e in l1:
    if e.endswith('s'):
        count+=1
print("Count of Strings which ends with 's':", count)
''' 