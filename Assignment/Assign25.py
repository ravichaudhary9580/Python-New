# Problem 1
# Write a python script to create a list of first N even natural numbers.
'''
l1 = [x for x in range(1,int(input("Enter a number:"))+1,1)]
print("List of N natural number:",l1)
'''

# Problem 2
# Write a python script to cleate a list of first N terms of Fibonacci series.
'''
l1 = [0,1]
for x in range(0,int(input("Enter a number:"))-2,1):
    l1.append(l1[x] + l1[x+1])
print(l1)
'''
'''
l1 = [0,1]
[l1.append(l1[x] + l1[x+1]) for x in range(0,int(input("Enter a number:"))-2,1)]
print(l1)
'''

# Problem 3
# Write a python script to create a list of first N prime numbers.
'''
n=int(input("Enter a number:"))
l1 = []
x=2
while n:
    for i in range(2,x,1):
        if x % i == 0:
            break
    else:
        l1.append(x) 
        n-=1
    x+=1
print(l1)
'''

# Problem 4
# Write a python script to add two matrices each of order 3x3. Store matrix elements in a list of lists.
''' 
print("Enter first matrix row wise:")
a=[
   [int(x) for x in input().split(',')],
   [int(x) for x in input().split(',')],
   [int(x) for x in input().split(',')]
   ]
print("Enter second matrix row wise:")
b=[
   [int(x) for x in input().split(',')],
   [int(x) for x in input().split(',')],
   [int(x) for x in input().split(',')]
   ]
c=[[0,0,0],[0,0,0],[0,0,0]]
print("Sum of Matrix A and B is:")
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]+b[i][j] 
        print(c[i][j],end=' ')
    print()
'''
# Problem 5
# Write a python script to create two lists from a given list of numbers in such a way that the first list can have only positive numbers and second list can have only non positive numbers.
print("Enter values with comma:")
a = [int(x) for x in input().split(',')]
positive = []
negative = []
for e in a:
    if e>=0:
        positive.append(e)
    else:
        negative.append(e)
print(positive)
print(negative)