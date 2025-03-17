import math

# Problem 1
# Write a program that swaps the values of variables a and b. You are not allowed to use a third variable. You are not allowed to perform arithmetic on a and b.
""" 
a=10   # 01010
b=20   # 10100
print(a,b)
a=a^b  # 01010 ^ 10100 --> 11110
b=a^b  # 11110 ^ 10100 --> 01010
a=a^b  # 11110 ^ 01010 --> 10100
print(a,b) 
"""


# Problem 2
# Write a program that makes use of trigonometric functions available in the math module.
""" 
# Example usage of trigonometric functions
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
print(f"Angle({angle_in_degrees} degrees) = {angle_in_radians} radians")

sin_value = math.sin(angle_in_radians)
cos_value = math.cos(angle_in_radians)
tan_value = math.tan(angle_in_radians)

print(f"sin({angle_in_degrees} degrees) = {sin_value}")
print(f"cos({angle_in_degrees} degrees) = {cos_value}")
print(f"tan({angle_in_degrees} degrees) = {tan_value}")
"""

# Problem 3
# Write a program that generates 5 random nubmers in the range 10 to 50. Use a seed value of 6. Make a provision to change this seed value every time you execute the program by associating it with time of execution?
""" 
import random
seed = input("Enter a seed value:")
# print(random.seed(seed))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50)) 
"""


# Problem 4
# Use trunc(), floor() and ceil() for numbers -2.8, -0,5, 0.2 , 1.5 and 2.9 to understand the difference between these function clearly.
import math
print("Use of trunc() function:")
print(-2.8,'---->', math.trunc(-2.8))
print(-0.5,'---->', math.trunc(-0.5))
print(0.2, '---->', math.trunc(0.2))
print(1.5, '---->', math.trunc(1.5))
print(2.9, '---->', math.trunc(2.9))

# Use of floor() function
print("Use of floor() function:")
print(-2.8,'---->', math.floor(-2.8))
print(-0.5,'---->', math.floor(-0.5))
print(0.2, '---->', math.floor(0.2))
print(1.5, '---->', math.floor(1.5))
print(2.9, '---->', math.floor(2.9))

# Use of ceil function
print("Use of ceil() function:")
print(-2.8,'---->', math.ceil(-2.8))
print(-0.5,'---->', math.ceil(-0.5))
print(0.2, '---->', math.ceil(0.2))
print(1.5, '---->', math.ceil(1.5))
print(2.9, '---->', math.ceil(2.9))
