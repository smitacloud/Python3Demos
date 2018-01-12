def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(numerator, denominator):
    return float(numerator) / denominator
'''
This module defines four mathematical functions: add, subtract, multiply and divide.
They do not do any error checking and they actually don’t do exactly what you might expect.
For example, if you were to call the add function with two strings,
it would happily concatenate them together and return them.
But for the purposes of illustration, this module will do for creating a test case.
So let’s actually write a test case for the add function!
We will call this script test_mymath.py and save it in the same folder that contains mymath.py.
'''
