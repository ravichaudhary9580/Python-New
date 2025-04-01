# Problem 1
# Write a python script to calculate sum of elements of a list.
'''
l1 = [10,20,30,40,50]
print(sum(l1))
l2 = [3.2,4.3,1.7]
print(sum(l2))
l3 = [3.2,4.3+1.7j]
print(sum(l3))
l4 = [True,True,False]
print(sum(l4))
'''

# Problem 2
# Write a python script to calculate average of elements of a list.
'''
l1 = [10,20,30,40,50]
print("Average:",sum(l1)/len(l1))
'''

# Problem 3
# Write a python script to crate a list of squares of numbers of a given list.
'''
print([ x**2 for x in range(1,int(input("Enter a number:"))+1,1)])
'''
'''
l1 = []
for e in range(1,int(input("Enter a number:"))+1,1):
    l1.append(e**2)
print(l1)
'''

# Program 4
# Write python script to sort list elements in descending order.
'''
l1 = [10, 20, 50, 40, 30, 90, 70, 60, 80]
print(sorted(l1, reverse=True))
'''

# Problem 5
# Write a python script to create a list from a given list by selecting only even places elements.
'''
l1 = list(range(1,21,3))
print(l1)
l2 = l1[1:11:2]
print(l2)
'''
print("Enter numbers seprated by comma:")
l1 = [int(e) for e in input().split(',')]
l2 = l1[1:11:2]
print(l2)