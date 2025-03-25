# Problem 1
# Write a Python script to calculate sum of first n natural numbers.
'''
N = int(input("Enter a number:"))
sum = 0
while N:
    sum += N
    N -=1
print("Sum:", sum)
'''
# Using for loop
'''
N = int(input("Enter a number:"))
sum = 0
num = range(1,N+1,1)
for e in num:
    sum += e
print("Sum:", sum)
'''

# Problem 2
# Write a Python script t calculate sum of squares of first N natural numbers.
'''
N = int(input("Enter a number:"))
sum = 0 
for e in range(1,N+1,1):
    sum += e*e
print("Sum:", sum)
'''

# Problem 3
# Write a Python script to calculate sum of cubes of first N natural numbers.
'''
N = int(input("Enter a number:"))
sum = 0 
for e in range(1,N+1,1):
    sum += e*e*e
print("Sum:", sum)
'''

# Problem 4
# Write a Python script to calculate sum of first N odd natural numbers.
'''
N = int(input("Enter a number:"))
sum = 0 
for e in range(1,2*N,2):
    sum += e
print("Sum:", sum)
'''

# Problem 5
# Write a Python script to calculate sum of first n even natural numbers.
'''
N = int(input("Enter a number:"))
sum = 0 
for e in range(2,2*(N+1),2):
    sum += e
print("Sum:", sum)
'''
