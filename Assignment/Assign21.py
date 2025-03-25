# Problem 1
# Write a python script to print first N even natural numbers.
'''
N = int(input("Enter a number:"))
num = range(2,2*(N+1),2)
for e in num:
    print(e,end=' ')
'''

# Problem 2
# Write a python script to print first N odd natural numbers.
'''
N = int(input("Enter a number:"))
num = range(1,2*N,2)
for e in num:
    print(e,end=' ')
'''

# Problem 3
# Write a python script to print square of first N natural numbers.
'''
N = int(input("Enter a number:"))
num = range(1,N+1,1)
for e in num:
    print(e*e,end=' ')

'''

# Problem 4
# Write a python script to print cubes of first N natural numbers.
'''
N = int(input("Enter a number:"))
num = range(1,N+1,1)
for e in num:
    print(e*e*e,end=' ')
'''

# Problem 5
# Write a python script to display all prime numbers within a range.
# range start = 15 end = 45
'''
num = range(15, 45, 2)
for e in num:
    i = e
    count = 0
    while i:
        if e % i == 0:
            count += 1
        i -= 1
    if count <= 2:
        print(e,end=' ')
'''