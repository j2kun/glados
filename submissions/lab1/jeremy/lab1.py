import math

def square(x):
   return x*x

def greet(name):
   return "Hello, " + name

def triangleArea(baseLength):
   return (1/2) * baseLength * 8

def discriminant(a, b, c):
   return b*b - 4 * a * c

def prodOfQuadraticSolutions(a,b,c):
   disc = discriminant(a,b,c)
   return ((-b + disc**0.5) / (2*a)) * ((-b - disc**0.5) / (2*a))

# cleverer!
#def prodOfQuadraticSolutions(a,b,c):
#   return c/a


def isMultipleOfPi(angle, tolerance):
   multiplesOfPi = angle / math.pi
   return abs(multiplesOfPi - round(multiplesOfPi)) < tolerance


def trigProblem(angle):
   if isMultipleOfPi(2*angle - math.pi/2, 0.001):
      return "Determine whether %.3f is in the domain of the function $f(\\theta) = \\tan(2 \\theta)$." % angle
   else:
      return "Solve the equation $\\tan(2 \\theta) = %.3f$ for $\\theta$" % math.tan(2*angle)
