"""
A script demonstrating python basics:
  - Importing libraries
  - Printing and string concatenation
  - Variable usage
  - Formatted output
  - Basci math
  - Command line arguments

This is a docstring: a multi-line string that begins/ends with three
double quotes (or single quotes).  For more info see https://peps.python.org/pep-0257/
"""

# Single line comments begin with a hash

# libraries and packages can be imported as follows
import sys
import math

# A basic print statement, endline characters are inserted by default:
print("Hello World")

# A basic print statement using the string concatenation operator, +:
print("Hello" + " " + "World")

#
# Basic variables
#
# Python is dynamically typed, so no declaration is necessary and
# a variable's type can change depending on what you assign to it.
# Python supports floating point numbers, integers, and strings
#

a = "forty two"
a = 42  # type has changed to an integer

# float:
b = 3.14

# Strings; you can use either double or single quotes:
c = "Hello"
c = 'Hello'

# Printing variable values:
print(a)
print(b)
print(c)

# Printing a variable that has not been set within the current scope is a
# *fatal* runtime error:
# print(d)

# Mixing types with string concatenation is a runtime error
# because only strings can be concatenated
#
# Error: print(c + " World!, a = " + a)
#
# However, you can convert any type to a string using str():

print(c + " World!, a = " + str(a))

# You can format variables in several ways; the modern way is to use
# f-strings (formatted strings).  Variables can be placed inside curly
# brackets and (optionally), printf-style formatting can be specified
# using a colon (ex: `{b:8.3f}` prints b as a floating point number
# with a minimum of 8 columns and 3 decimals of precision):

print(f"{c} World!, a = {a}, b = {b:8.3f}, a = {a:05}")

# some basic math library math:

a = 1.5
b = 20
c = 3.5

# floating point numbers in Python are 64-bit IEEE-754 floats (16-17 digits of precision),
# but libraries (Decimal) support arbitrary precision operations
y = math.sqrt(b*b - 4*a*c)
print(f"y = {y}")

# Python natively supports arbitrarily large integers
y = 2**100
print(f"y = {y}")

# Basic command line arguments (CLAs) are supported in the sys library.
#
# Number of command line arguments:
n = len(sys.argv)

# The script file name is always the first one (index 0): sys.argv[0]
# Print the argv as a list:
print(sys.argv)
# Print each argument using a loop:
for i in range( len(sys.argv) ):
    print(f"sys.argv[{i}] = {sys.argv[i]}")

# You can convert CLAs (strings) using int() or float(); you can check if
# a string represents a valid digit prior to conversion using isdigit():
#
if n >= 2:
    if sys.argv[1].isdigit():
        x = int(sys.argv[1])
        print(f"command line argument converted to integer: {x}")
    else:
        print(f"command line argument is not convertable to integer: {sys.argv[1]}")

if n >= 3:
    if sys.argv[2].isdigit():
        y = float(sys.argv[2])
        print(f"command line argument converted to float: {y}")
    else:
        print(f"command line argument is not convertable to float: {sys.argv[2]}")
