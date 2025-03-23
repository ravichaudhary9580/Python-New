# Problem 1
# Write a python script to check whether a given number is a three digit number or not.
'''
x = int(input("Enter a number:"))
match x:
    case x if 99<x<1000:
        print("Three digit number.")
    case _:
        print("NOT a three digit number.")
'''

# Problem 2
# Write a python script to check whether a given numver is positive, negative or zero.
'''
x = int(input("Enter a number:"))
match x:
    case x if x>0:
        print("Positive")
    case x if x<0:
        print("Negative")
    case x if x==0:
        print("Zero")
'''

# Problem 3
# Write a python script to make a menu driven program in which user has to choose one of the options - 1) Odd-Even, 2) Positive - Non-Positive, 3) Simple Interest and 4) Find roots of quadratic equation. Match and execute appropriate code on user selection.
'''
print('\033[32m********************************************\033[0m')
print("# Menu -- \033[32mSelect an Option\033[0m")
print("1) Odd - Even")
print("2) Positive - Non-Positive")
print("3) Simple Interest")
print("4) Find roots of quadratic equation")
print("\033[31m5) Exit\033[0m")

option = int(input("Enter Option:"))

match option:
    case 1:
        num = int(input("Enter a number:"))
        if num % 2:
            print("Odd Number")
        else:
            print("Even Number")
    case 2:
        num = int(input("Enter a number:"))
        if num > 0:
            print("Positive Number")
        elif num < 0:
            print("Negative Number")
        else:
            print("Zero")
    case 3:
        p = float(input("Enter Principle:"))
        r = float(input("Enter Rate:"))
        t = float(input("Enter Time:"))
        si = (p*r*t)/100
        print("Simple Interest:", si)
    case 4:
        import math
        print("Genral form of quadratic equation is \033[31max²+bx+c=0\033[0m")
        a = int(input("Enter the coffiecient of x²: "))
        b = int(input("Enter the coffiecient of x: "))
        c = int(input("Enter the constant: "))
        D = b**2-4*a*c
        if D<0: 
            print("\033[33mRoots are Imaginary\033[0m")
            print('Root1= (',-b,'+',-D,'j)','/','2a')
            print('Root2= (',-b,'-',-D,'j)','/','2a')
        elif D==0:
            print("\033[33mRoots are Real and Equal\033[0m")
            r1 = -b/(2*a)
            r2 = -b/(2*a)
            print("Roots are: ",r1,r2)
        else :
            print("\033[33mRoots are Real and Distinct\033[0m")    
            r1 = (-b+math.sqrt(D))/(2*a)
            r2 = (-b-math.sqrt(D))/(2*a)
            print("Roots are: ",r1,r2)       
    case 5:
        print("\033[31mProgram End\033[0m")
        exit()
    case _:
        print("\033[31mInvalid Input Try Again\033[0m")
'''

# Problem 4
# Write a python script to take one data from user and evaluate the type of data. If the data is of int type then print Monday, if the data is of Float print Tuseday, if the data is of complex type then print Wednesday, if the data is of type bool then print Thrusday.
'''
x = eval(input("Enter a Number:"))

match x:
    case x if type(x) == int:
        print("Monday")
    case x if type(x) == float:
        print("Tuesday")
    case x if type(x) == complex:
        print("Wednesday")
    case x if type(x) == bool:
        print("Thrusday")
'''
   
   
# Problem 5
# Write a python script to take a string from the user. If the string is a part of "mysirg" then print "One", if the string is a part of "education" then print "Two" and if the string is a part of "services" then print "Three".
'''
string = input("Enter a string:")
match string:
    case string if string in "mysirg":
        print("One")  
    case string if string in "education":
        print("Two")  
    case string if string in "services":
        print("Three")  
'''