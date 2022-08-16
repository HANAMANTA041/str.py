#declared using 'x'or "x"
#multiline string """x""" or '''x'''
x= """Oranges 
ARE ORANGE IN 
COLOUR
"""

print(x)
y= "hello, world!   "#Strings in python are arrays that represents unicode chracter
print(y)
print(len(y))# we can access the character from the string by []
print("the" in y)
print("meet" in y)# in function gives boolean result ,check certain value inside a srting
print(y[5])# char positions
#for a in y: #loop through a string
 #   print(a)
print(y[2:5])#slice a string:take certain part of the string to print only that
print(y[:12])
print(y[5:])
print(y[-5:-2])#negative indexing  prints orl
print(y.upper())#modify string using .upper
print(y.lower())
print(y.strip())#remove white spaces
print(y.replace("h", "y"))#replace a certain string
print(y.split(","))#split a string
#string concatenation
a="Hello"
b="World"

print(a+b)# without space in between
print(a+" "+b)
#string methods
#Escape characters


