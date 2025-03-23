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
'''
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
'''

# Problem 5
# Assume a suitable value for temperature of a city in Fahrenheit degrees. Write a program to covert this temperature into Centigrade degrees and print both temperature.
'''
import random
Fahrenheit = random.randint(70,120) # assuming and picking a temp value
Centigrade = (5/9)*(Fahrenheit-32)
print("Temperature in Fahrenheit:",Fahrenheit)
print("Temperature in Centigrade:",Centigrade)
'''

# Problem 6
# Given three sides a, b, c of a triangle, write a program to obtainand print the values of three angles rounded to the next integer . Use the formulae:
# a² = b² + c² -2bc cos(A)
# b² = a² + c² -2ac cos(B)
# c² = a² + b² -2ab cos(C)
# cos(A) = (b**2 + c**2 - a**2)/2*b*c
# cos(B) = (a**2 + c**2 - b**2)/2*a*c
# cos(C) = (a**2 + b**2 - c**2)/2*a*b

'''
print("Enter the sides of Triangle:")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

cos_value_A = (b**2 + c**2 - a**2)/(2*b*c)
cos_value_B = (a**2 + c**2 - b**2)/(2*a*c) 
cos_value_C = (a**2 + b**2 - c**2)/(2*a*b)

angle_radians_A = math.acos(cos_value_A)
angle_radians_B = math.acos(cos_value_B)
angle_radians_C = math.acos(cos_value_C)

angle_degrees_A = math.degrees(angle_radians_A)
angle_degrees_B = math.degrees(angle_radians_B)
angle_degrees_C = math.degrees(angle_radians_C)

print("Angle A in radians:", angle_radians_A, "Angle A in degrees:", angle_degrees_A)
print("Angle B in radians:", angle_radians_B, "Angle B in degrees:", angle_degrees_B)
print("Angle C in radians:", angle_radians_C, "Angle C in degrees:", angle_degrees_C)
'''


# [B] How will you perform the following operations?
# (a) Print imaginary part out of 2+3j.
"""
x = 2+3j
print(x.imag)
"""
# (b) Obtain conjugate of 4+2j.
'''
x = 4+2j
print(x.conjugate())
'''
# (c) Print decimal equivalent of binary '1100001110'.
'''
print(0b1100001110)
'''
# (d) Convert a float value 4.33 into a numeric string.
'''
x = str(4.33)
print(x,type(x))
'''
# (e) Obtain integer quotient and remainder while dividing 29 with 5
'''
quotient = 29//5
remainder = 29%5
print(quotient, remainder)
'''
# (f) Obtain hexadecimal equivalent of decimal 34567.
'''
print(hex(34567))
'''
# (g) Round-off 45.6782 to second decimal place.
'''
x = 45.6782
print(round(x,2))
'''
# (h) Obtain 4 from 3.556
'''
x = 3.556
print(int(round(x,0)))
'''
# (i) Obtain 17 from 16.7844
'''
x = 16.7844
print(int(round(x,0)))
'''
# (j) Obtain remainder on dividing 3.45 with 1.22.
'''
r = 3.45%1.22
print(r)
'''

# [C] Which of the following is invalid variable name and why?
#            VALID                    INVALID
#         BASICSALARY                basic-hra        
#           _basic                     #MEAN
#            over                      group.
#      timemindovermatter               422
#           SINGLE                  pop in 2020 
#            hELLO                  team'svictory
#            queue                    Plot # 3
#          2015_DDay



# [D] Evaluate the following expressions.
# (a) 2**6/8%2 -----> 0.0
# (b) 9**2//5-3 ----> 13
# (c) 10+6-2%3+7-2 ----> 19
# (d) 5%10+10-23*4//3 ----> -15
# (e) 5+5//5-5*5**5%5 ----> 6
# (f) 7%7+7//7-7*7 ----> -48


# [E] Evaluate the following expressions:
# (a) min(2,6,8,5)
# print(min(2,6,8,5)) ----> 2
# (b) bin(46)
# print(bin(46)) ---->   '0b101110'
# (c) round(10.544336,2)
# print(round(10.544336,2)) -----> 10.54
# (d) math.hypot(6,8)
# print(math.hypot(6,8))  -----> 10.0
# (e) math.modf(3.1415)
# print(math.modf(3.1415))  -----> (0.14150000000000018, 3.0)


# [F] Match the following pairs:
#     a. complex                   ------>    3. Basic Type
#     b. Escape special character  ------>    1. \
#     c. Tuple                     ------>    2. Container type
#     d. Natural Logarithm         ------>    4. log()
#     e. Common logarithmlog10()   ------>    5. log10()