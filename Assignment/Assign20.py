# Problem 1
# Write a python script to print first 10 multiple of 5.
'''
num = range(1,11,1)
for i in num:
    print(5*i,end=' ')
'''

# Problem 2
# Write a python script to print first 10 multiple of N.
'''
num = range(1,11,1)
N = int(input("Enter a number:"))
for i in num:
    print(N*i,end=' ')
'''

# Problem 3
# Write a python script to print first M multiple of N.
'''
N = int(input("Enter a number:"))
M = int(input("Enter the number of Multiples:"))
num = range(1,M+1,1)
for i in num:
    print(N*i,end=' ')
'''

# Problem 4
# Write a python script to print first 10 multiple of N in reverse order.
'''
N = int(input("Enter a number:"))
num = range(10,0,-1)
for i in num:
    print(N*i,end=' ')
'''

# Problem 5
# Write a python script to print table of user choice.
'''
N = int(input("Enter a number:"))
num = range(1,11,1)
for i in num:
    print(N,'x',i,'=',N*i)
'''
