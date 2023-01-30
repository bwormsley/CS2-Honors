"""
A collection statistics-related functions that operate on
lists of numbers.

Note: we've named our functions minimum(), maximum(), and sumVals()
because python already has min(), max(), and sum() functions that
are built-in.  In general, those functions should be used instead of
these (we've only done this to demonstrate basic functionality and
unit testing).
"""
import math

def minimum(values):
    """Finds and returns the minimal element in the given list
    of values.
    """
    minVal = math.inf
    for x in values:
        if x < minVal:
            minVal = x
    return minVal

def maximum(values):
    """Finds and returns the maximum element in the given list
    of values
    """
    maxVal = -(math.inf)
    for x in values:
        if x > maxVal:
            maxVal = x
    return maxVal

def sumVals(values):
    """Computes the sum of all elements the given list 
    of values
    """
    sum = 0
    for i in range(len(values)):
        sum  += values[i]
    return sum

def mean(values):
    """Computes the mean value of the numbers in the given list
    of values.
    """
    return sum(values) / len(values)