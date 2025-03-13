import A1 # This method is used to import the whole file.
print(A1.a)

from A1 import a # This method is used to import selected elements.
print(a)

from A1 import a as x # This method is used to import selected element and change the element name how they known in this file.
print(x)