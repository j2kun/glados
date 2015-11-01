import math

def square(x):
   return x*x

def greet(name):
   return "Hello, "+name

def triangleArea(base):
   return (1/2)*base*8

def discriminant(a,b,c):
   return square(b)-(4*a*c)

def prodOfQuadraticSolutions(a,b,c):
   x1=(-b+(discriminant(a,b,c))**0.5)/(2*a)
   x2=(-b-(discriminant(a,b,c))**0.5)/(2*a)
   return x1*x2

def isMultipleOfPi(x,e):
   y=x/math.pi
   z=round(y)
   if abs(y-z)<=e:
      return True
   else:
      return False

def trigProblem(a):
   b=(2*a)-(math.pi/2)
   if isMultipleOfPi(b,0.001)==True:
      return "Determine whether %.3f is in the domain of the function $f(\\theta) = \\tan(2 \\theta)$." %(a)
   else:
      t=math.tan(2*a)
      return "Solve the equation $\\tan(2 \\theta) = %.3f$ for $\\theta$."%(t)
   



               
