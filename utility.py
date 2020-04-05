import math

'''
Utility functions used to perform simple operations on tuple based vectors
'''

# Addition
def tadd(a, b):
  return (a[0] + b[0], a[1] + b[1])

# Subtraction
def tsub(a, b):
  return (a[0] - b[0], a[1] - b[1])

# Multiplication by a scalar
def tmul(a, b):
  return (a[0] * b, a[1] * b)

# Division by a scalar
def tdiv(a, b):
  return (a[0] / b, a[1] / b)

# Returns the distance between two vectors
def tdist(a,b):
    return math.sqrt(((a[0] - a[1]) ** 2) + ((b[0] - b[1]) ** 2))
