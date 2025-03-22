# Problem 1
# Write a python script to check whether a given number is a three digit number or not.
'''
num = int(input("Enter a number: "))
if 99<num<1000:    # 99<num and num<1000    chained comparision
    print("Three digit number.")
else:
    print("NOT a three digit number.")
'''

# Problem 2
# Write a python script to check whether a given number is positive, negative or zero.
'''
num = int(input("Enter a number: "))
if num<0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")
'''

# Problem 3
# Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
'''
print("Genral form of quadratic equation is \033[31max²+bx+c=0\033[0m")
a = int(input("Enter the coffiecient of x²: "))
b = int(input("Enter the coffiecient of x: "))
c = int(input("Enter the constant: "))

D = (b**2)-(4*a*c)

if D > 0:
    print("Equation has \033[32mReal & Distinct\033[0m roots.")
elif D == 0:
    print("Equation has \033[32mReal & Equal\033[0m roots.")
else:
    print("Equation has \033[32mImaginary\033[0m roots.")
'''

# Problem 4
# Write a python script to whether a given year is leap or not.
'''
year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")
    else:
        print("NOT a Leap year")
elif year % 4 == 0:
    print("Leap year")

else:
    print("NOT a Leap year")
'''
 
# Problem 5
# Write a python script to print greater among three numbers. Print number only once even if the  numbers are the same.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
 
# greatest = a if a>b else b if b>c else c
# print(greatest)  

# if a>=b and a>=c:
#     print(a,'a')
# elif b>=a and b>=c:
#     print(b,'b')
# else:
#     print(c,'c')

# print(max(a,b,c))
'''
