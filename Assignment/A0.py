import A1 # This method is used to import the whole file.
print(A1.a)

from A1 import a # This method is used to import selected elements.
print(a)

from A1 import a as x # This method is used to import selected element and change the element name how they known in this file.
print(x)


# Problem 1 --- loop
# Print all the character of string, but stop printing if 'r' appeared in the sequence If all the character successfully printed then print message "All the characters are processed".
'''
string = input("Enter a string:")
for e in string:
    if e == 'r':
        break
    print(e)
else:
    print("All the characters are processed.")
'''

