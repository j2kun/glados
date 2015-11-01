# this is lab 1
import math

def square(num):
   return num**2

def greet(name):
   return "Hello, " + name

def triangleArea(base):
   height = 8
   return .5*base*height  

def discriminant(a, b, c):
   #a, b, c are coefficients of 0 = ax^2+bx+c
   return b**2-4*a*c

def prodOfQuadraticSolutions(a, b, c):
   disc = discriminant(a, b, c)
   root1 = (-b + (disc)**0.5)/(2*a)
   root2 = (-b - (disc)**0.5)/(2*a) 
   
   return root1*root2

def isMultipleOfPi(theta, E):
   #Test if theta is within error E of a multiple of pi
   
   nearestMultiple = round(theta/math.pi)
   return abs( theta - nearestMultiple*math.pi)<E
   
def trigProblem(angle):
   Q = math.tan(2*angle)
   if isMultipleOfPi(2*angle - math.pi/2 , 0.001): 
   # Test if theta is within 0.001 of a multiple of pi/2   
       
      return "Determine whether %.3f is in the domain of the function $f(\\theta) = \\tan(2 \\theta)$." %angle


   else:
      return "Solve the equation $\\tan(2 \\theta) = %.3f$ for $\\theta$." %Q


