

def add(a ,b):
   return a + b
    

def subtract(a,b):
    if a>b:
      return  a-b
    else:
        print(" negative answer, ensure a >= b")


def percentage(a , b ):
   return a/b *100

def fraction(a,b):
   return float(a/b)

import math

def squareroot(a):
   return math.sqrt(a)

def cuberoot(a):
   return math.cbrt(a)

def division(a, b):
   if b != 0:
      return a/b
   else:("Error! can not be divided by zeero")

def Exponential(a, b):
   return a**b

def multiply(a,b,c,):
   return a * b *c

print(add(4,6))
print(subtract(6,2))
print(percentage(1,10))
print(fraction(3,2))
print (squareroot(9))
print(squareroot(16))
print(cuberoot(27))
print(Exponential(2,3))
print(multiply(3,4,6))



