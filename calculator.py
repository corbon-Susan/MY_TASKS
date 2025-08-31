

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

choice= input("Type a number to do your calculations \n1= \tadd, \n2 = \tsubtract, \n3 = \tpercentage, \n4 =" 
" \tExponential, \n5 = \tSquareroot, \n6 = \tCuberoot, \n7 = \tDivision, \n8 = \tMultiply, \n9 = \t Fraction \n0 = \t Exit")

num1 = float(int(input("Enter a number: " )))
num2 = float(int(input("Enter a number: ")))

if  choice == '1':
   print(f"Addition of numbers {num1} + {num2} =", add(num1, num2))
elif choice == "2":
   print(f"Subtraction of numbers {num1} - {num2} =", subtract (num1, num2))




#print (choice)
# print(add(4,6))
# print(subtract(6,2))
# print(percentage(1,10))
# print(fraction(3,2))
# print (squareroot(9))
# print(squareroot(16))
# print(cuberoot(27))
# print(Exponential(2,3))
# print(multiply(3,4,6))



