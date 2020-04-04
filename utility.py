import math

def tadd(a, b):
  return (a[0] + b[0], a[1] + b[1])

def tsub(a, b):
  return (a[0] - b[0], a[1] - b[1])

def tmul(a, b):
  return (a[0] * b, a[1] * b)

def tdiv(a, b):
  return (a[0] / b, a[1] / b)

def tdist(a,b):
    return math.sqrt(((a[0] - a[1]) ** 2) + ((b[0] - b[1]) ** 2)) 
