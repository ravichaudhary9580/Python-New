# Problem 3.1
# Demonstrate the use of integer types and operators that can be used on them.
'''
# Use of integer types
print(3/4) # 0.75
print(3%4) # 3
print(3//4) # 0
print(3**4) # 81
print(4/2)  # 2.0
print(7%2)  # 1
print(4//3) # 1
print("True Division")
print(10/3)     #  3.333333333
print(-10/3)    # -3.333333333
print(10/-3)    # -3.333333333
print(-10/-3)   #  3.333333333
print(3/10)     #  0.3
print(3/-10)    # -0.3
print(-3/10)    # -0.3
print(-3/-10)   #  0.3
print("Floor Division")
print(10//3)    #  3
print(-10//3)   # -4  floor function returns the integer less than or equal to the given number.
print(10//-3)   # -4
print(-10//-3)  #  3
print(3//10)    #  0
print(3//-10)   # -1
print(-3//10)   # -1
print(-3//-10)  #  0
print("Modulus Division")   # x = a-(b*(a//b))  is used to evaluate a % b
print(10%3)     #  1
print(-10%3)    #  2    = -10-(3*(-10//3))  --> = -10-(3*(-4))  --> = -10-(-12) --> = -10+12 --> =  2
print(10%-3)    # -2    =  10-(-3*(10//-3)) --> =  10-(-3*(-4)) --> =  10-(12)  --> =  10-12 --> = -2
print(-10%-3)   # -1    = -10-(-3*(-10//-3))--> = -10-(-3*(3))  --> = -10-(-9)  --> = -10+9  --> = -1
print(3%10)     #  3
print(3%-10)    # -7    =  3-(-10*(3//-10)) --> =  3-(-10(-1)) --> =  3-(10)  --> =  3-10 --> = -7
print(-3%10)    #  7    = -3-(10*(-3//10))  --> = -3-(10*(-1)) --> = -3-(-10) --> = -3+10 --> = 7 
print(-3%-10)   # -3    = -3-(-10*(-3//-10))--> = -3-(-10*(0)) --> = -3-(0)   --> = -3
'''


# Problem 2
# Demonstrate the use of int, float, complex, bool and str types and operators that can be used on them.
'''
# Use of int types
print(3 + 4)  # 7
print(3 - 4)  # -1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(3 % 4)  # 3
print(3 // 4) # 0
print(3 ** 4) # 81

# Use of float types
print(3.5 + 2.1)  # 5.6
print(3.5 - 2.1)  # 1.4
print(3.5 * 2.1)  # 7.35
print(3.5 / 2.1)  # 1.6666666666666667
print(3.5 // 2.1) # 1.0
print(3.5 % 2.1)  # 1.4
print(3.5 ** 2.1) # 17.378008287493755

# Use of complex types
c1 = 2 + 3j
c2 = 1 + 2j
print(c1 + c2)  # (3+5j)
print(c1 - c2)  # (1+1j)
print(c1 * c2)  # (-4+7j)
print(c1 / c2)  # (1.6-0.2j)
print(c1.real)  # 2.0
print(c1.imag)  # 3.0

# Use of bool types
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
print(True + True)     # 2
print(True * False)    # 0

# Use of str types
print("Hello" + " World")  # Hello World
print("Hello" * 3)         # HelloHelloHello
print("Hello"[1])          # e
print("Hello"[1:4])        # ell
print("Hello".upper())     # HELLO
print("Hello".lower())     # hello
print("Hello".replace("e", "a"))  # Hallo


# List of all the operators used in Python
operators = [
    '+', '-', '*', '/', '//', '%', '**',  # Arithmetic operators   7
    '==', '!=', '>', '<', '>=', '<=',     # Comparison operators   6
    'and', 'or', 'not',                   # Logical operators      3
    '&', '|', '^', '~', '<<', '>>',       # Bitwise operators      6
    '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=', '&=', '|=', '^=', '>>=', '<<='  # Assignment operators     13
]

print("Operators used in Python:", operators)

# Arithmetic operators with int, float, complex, bool, and str types

# With int types
print(3 + 4)  # 7
print(3 - 4)  # -1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(3 % 4)  # 3
print(3 // 4) # 0
print(3 ** 4) # 81

# With float types
print(3.5 + 2.1)  # 5.6
print(3.5 - 2.1)  # 1.4
print(3.5 * 2.1)  # 7.35
print(3.5 / 2.1)  # 1.6666666666666667
print(3.5 // 2.1) # 1.0
print(3.5 % 2.1)  # 1.4
print(3.5 ** 2.1) # 17.378008287493755

# With complex types
c1 = 2 + 3j
c2 = 1 + 2j
c3 = 2 + 3j
print(c1 + c2)  # (3+5j)
print(c1 - c2)  # (1+1j)
print(c1 * c2)  # (-4+7j)
print(c1 / c2)  # (1.6-0.2j)

# With bool types
print(True + False)  # 1
print(True - False)  # 1
print(True * False)  # 0
print(True / True)   # 1.0

# With str types
print("Hello" + " World")  # Hello World
print("Hello" * 3)         # HelloHelloHello


# Comparison operators with int, float, complex, bool, and str types

# With int types
print(3 == 4)          # False
print(3 != 4)          # True
print(3 > 4)           # False
print(3 < 4)           # True
print(3 >= 4)          # False
print(3 <= 4)          # True

# With float types
print(3.5 == 3.5)      # True
print(3.5 != 3.5)      # False
print(3.5 > 2.1)       # True
print(3.5 < 2.1)       # False
print(3.5 >= 2.1)      # True
print(3.5 <= 2.1)      # False

# With complex types
# In Python, comparison operators such as == and != can be used with complex numbers, but other comparison operators like <, >, <=, and >= are not supported for complex numbers. This is because complex numbers do not have a natural ordering.
# Equality and inequality comparisons
print(c1 == c2)  # False
print(c1 == c3)  # True
print(c1 != c2)  # True
print(c1 != c3)  # False

# With bool types
print(True == False)   # False
print(True != False)   # True
print(True > False)    # True
print(True < False)    # False

# With str types
print("Hello" == "World")  # False
print("Hello" != "World")  # True
print("Hello" > "World")   # False
print("Hello" < "World")   # True
print("Hello" >= "World")  # False
print("Hello" <= "World")  # True




# Logical operators with int, float, complex, bool, and str types
# With int types
print(3 and 4)          # 4
print(3 or 4)           # 3
print(not 3)            # False

# With float types
print(3.5 and 2.1)      # 2.1
print(3.5 or 2.1)       # 3.5
print(not 3.5)          # False

# With complex types
print((2+3j) and (1+2j))  # (1+2j)
print((2+3j) or (1+2j))   # (2+3j)
print(not (2+3j))         # False

# With bool types
print(True and False)    # False
print(True or False)     # True
print(not True)          # False

# With str types
print("Hello" and "World")  # World
print("Hello" or "World")   # Hello
print(not "Hello")          # False



# Bitwise operators with int, bool types
# Bitwise operations are not available for float, complex, and str types
# With int types
print(3 & 4)   # 0
print(3 | 4)   # 7
print(3 ^ 4)   # 7
print(~3)      # -4
print(3 << 2)  # 12
print(3 >> 2)  # 0

# With bool types
print(True & False)  # False
print(True | False)  # True
print(True ^ False)  # True
print(~True)         # -2
print(True << 2)     # 4
print(True >> 2)     # 0
'''


# Problem 3
# Demonstrate how to convert one number type to another: bool, int, float, complex and String
'''
# Converting to bool
print(bool(0))       # False
print(bool(1))       # True
print(bool(-1))      # True
print(bool(0.0))     # False
print(bool(0.1))     # True
print(bool(1+1j))    # True
print(bool(0+0j))    # False

# Converting to int
print(int(True))     # 1
print(int(False))    # 0
print(int(3.5))      # 3
print(int(-3.5))     # -3
print(int(1+2j))     # TypeError: can't convert complex to int

# Converting to float
print(float(True))   # 1.0
print(float(False))  # 0.0
print(float(3))      # 3.0
print(float(-3))     # -3.0
print(float(1+2j))   # TypeError: can't convert complex to float

# Converting to complex
print(complex(True))   # (1+0j)
print(complex(False))  # (0+0j)
print(complex(3))      # (3+0j)
print(complex(3.5))    # (3.5+0j)
print(complex(1, 2))   # (1+2j)

# Converting to str
print(str(True))       # 'True'
print(str(False))      # 'False'
print(str(3))          # '3'
print(str(3.5))        # '3.5'
print(str(1+2j))       # '(1+2j)'

# Converting from str to bool
print(bool("True"))    # True
print(bool("False"))   # True (non-empty strings are considered True)
print(bool(""))        # False (empty string is considered False)

# Converting from str to int
print(int("123"))      # 123
print(int("-123"))     # -123
print(int("123.45")) # ValueError: invalid literal for int() with base 10: '123.45'
print(int("abc"))    # ValueError: invalid literal for int() with base 10: 'abc'

# Converting from str to float
print(float("123.45")) # 123.45
print(float("-123.45"))# -123.45
print(float("abc"))  # ValueError: could not convert string to float: 'abc'

# Converting from str to complex
print(complex("1+2j")) # (1+2j)
print(complex("1-2j")) # (1-2j)
print(complex("1.5+2.5j")) # (1.5+2.5j)
print(complex("abc")) # ValueError: could not convert string to complex: 'abc'
'''


# Problem 4
# Demonstrate the use of built-in mathematical functions.
'''
import math
import random
# Constants
print("Math constants:")
print("Pi:", math.pi)  # 3.141592653589793
print("Euler's number:", math.e)  # 2.718281828459045

# Trigonometric functions
print("\nTrigonometric functions:")
print("sin(pi/2):", math.sin(math.pi / 2))  # 1.0
print("cos(pi):", math.cos(math.pi))  # -1.0
print("tan(pi/4):", math.tan(math.pi / 4))  # 1.0

# Inverse trigonometric functions
print("\nInverse trigonometric functions:")
print("asin(1):", math.asin(1))  # 1.5707963267948966 (pi/2)
print("acos(1):", math.acos(1))  # 0.0
print("atan(1):", math.atan(1))  # 0.7853981633974483 (pi/4)

# Hyperbolic functions
print("\nHyperbolic functions:")
print("sinh(1):", math.sinh(1))  # 1.1752011936438014
print("cosh(1):", math.cosh(1))  # 1.5430806348152437
print("tanh(1):", math.tanh(1))  # 0.7615941559557649

# Exponential and logarithmic functions
print("\nExponential and logarithmic functions:")
print("exp(1):", math.exp(1))  # 2.718281828459045
print("log(10):", math.log(10))  # 2.302585092994046
print("log10(10):", math.log10(10))  # 1.0
print("log2(8):", math.log2(8))  # 3.0

# Power and square root functions
print("\nPower and square root functions:")
print("sqrt(16):", math.sqrt(16))  # 4.0
print("pow(2, 3):", math.pow(2, 3))  # 8.0

# Rounding functions
print("\nRounding functions:")
print("ceil(4.2):", math.ceil(4.2))  # 5
print("floor(4.8):", math.floor(4.8))  # 4
print("trunc(4.8):", math.trunc(4.8))  # 4

# Factorial and combinatorial functions
print("\nFactorial and combinatorial functions:")
print("factorial(5):", math.factorial(5))  # 120
print("gcd(48, 18):", math.gcd(48, 18))  # 6

# Miscellaneous functions
print("\nMiscellaneous functions:")
print("degrees(pi):", math.degrees(math.pi))  # 180.0
print("radians(180):", math.radians(180))  # 3.141592653589793
'''


# Problem 5
# Demonstrate the use of functions in the math module.
'''
# Constants
print("Math constants:")
print("Pi:", math.pi)  # 3.141592653589793
print("Euler's number:", math.e)  # 2.718281828459045

# Trigonometric functions
print("\nTrigonometric functions:")
print("sin(pi/2):", math.sin(math.pi / 2))  # 1.0
print("cos(pi):", math.cos(math.pi))  # -1.0
print("tan(pi/4):", math.tan(math.pi / 4))  # 1.0

# Inverse trigonometric functions
print("\nInverse trigonometric functions:")
print("asin(1):", math.asin(1))  # 1.5707963267948966 (pi/2)
print("acos(1):", math.acos(1))  # 0.0
print("atan(1):", math.atan(1))  # 0.7853981633974483 (pi/4)

# Hyperbolic functions
print("\nHyperbolic functions:")
print("sinh(1):", math.sinh(1))  # 1.1752011936438014
print("cosh(1):", math.cosh(1))  # 1.5430806348152437
print("tanh(1):", math.tanh(1))  # 0.7615941559557649

# Exponential and logarithmic functions
print("\nExponential and logarithmic functions:")
print("exp(1):", math.exp(1))  # 2.718281828459045
print("log(10):", math.log(10))  # 2.302585092994046
print("log10(10):", math.log10(10))  # 1.0
print("log2(8):", math.log2(8))  # 3.0

# Power and square root functions
print("\nPower and square root functions:")
print("sqrt(16):", math.sqrt(16))  # 4.0
print("pow(2, 3):", math.pow(2, 3))  # 8.0

# Rounding functions
print("\nRounding functions:")
print("ceil(4.2):", math.ceil(4.2))  # 5
print("floor(4.8):", math.floor(4.8))  # 4
print("trunc(4.8):", math.trunc(4.8))  # 4

# Factorial and combinatorial functions
print("\nFactorial and combinatorial functions:")
print("factorial(5):", math.factorial(5))  # 120
print("gcd(48, 18):", math.gcd(48, 18))  # 6

# Miscellaneous functions
print("\nMiscellaneous functions:")
print("degrees(pi):", math.degrees(math.pi))  # 180.0
print("radians(180):", math.radians(180))  # 3.141592653589793
'''


# Problem 6
# Write a program that generates float and integer random numbers.
""" 
import random
# Generate a random float number between 0 and 1

print("Random float between 0 and 1:", random.random())
print("Random float between 0 and 1:", random.random())
print("Random float between 0 and 1:", random.random())
print("Random float between 0 and 1:", random.random())

# Generate a random integer between a given range
print("Random integer between 1 and 100:", random.randint(1, 100))
print("Random integer between 1 and 100:", random.randint(1, 100))
print("Random integer between 1 and 100:", random.randint(1, 100))
print("Random integer between 500 and 1000:", random.randint(500, 1000))
print("Random integer between 500 and 1000:", random.randint(500, 1000))
print("Random integer between 500 and 1000:", random.randint(500, 1000))
"""

