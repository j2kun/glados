from .testrunner import TestSuite
import math

class Grader(TestSuite):
   def __init__(self, *modules):
      super(Grader, self).__init__()

      (m,) = modules
      self.expectedModules = ["square", "greet", "triangleArea", "discriminant", 
         "prodOfQuadraticSolutions", "isMultipleOfPi", "trigProblem"]
      self.assertAttributesExist(m, *self.expectedModules)

      for fName in self.expectedModules:
         setattr(self, fName, getattr(m, fName))
   
   def testSquare1(self):
      self.test(1, self.square, 1)

   def testSquare2(self):
      self.test(169, self.square, 13)

   def testSquare3(self):
      self.test(4, self.square, -2)

   def testGreet1(self):
      self.test("Hello, Jeremy", self.greet, "Jeremy")

   def testGreet2(self):
      self.test("Hello, ", self.greet, "")

   def testGreet3(self):
      self.test("Hello, silly goose!", self.greet, "silly goose!")
   
   def testTriangleArea1(self):
      self.test(8, self.triangleArea, 2)

   def testTriangleArea2(self):
      self.test(0, self.triangleArea, 0)

   def testTriangleArea3(self):
      self.test(32, self.triangleArea, 8)

   def testDiscriminant1(self):
      self.test(-8, self.discriminant, 1, 2, 3)

   def testDiscriminant2(self):
      self.test(17, self.discriminant, -1, 3, 2)

   def testDiscriminant3(self):
      self.test(0, self.discriminant, 3, 6, 3)

   def testDiscriminant4(self):
      self.test(0, self.discriminant, 0, 0, 0)

   def testProdQuad1(self): 
      self.test(-6.0, self.prodOfQuadraticSolutions, 1, 5, -6, floatComparison=True)

   def testProdQuad2(self):
      self.test(-6.0, self.prodOfQuadraticSolutions, 1, 10, -6, floatComparison=True)

   def testProdQuad3(self): # multiple root
      self.test(1.0, self.prodOfQuadraticSolutions, 1, 2, 1, floatComparison=True)

   def testProdQuad4(self):
      self.test(-512.0, self.prodOfQuadraticSolutions, 2, 20, -1024, floatComparison=True)

   def testIsMultipleOfPi1(self):
      self.test(False, self.isMultipleOfPi, 2, 0.001)

   def testIsMultipleOfPi2(self):
      self.test(True, self.isMultipleOfPi, math.pi, 0.001)

   def testIsMultipleOfPi3(self):
      self.test(True, self.isMultipleOfPi, -7*math.pi, 0.001)

   def testIsMultipleOfPi4(self):
      self.test(True, self.isMultipleOfPi, math.pi*math.pi, 0.5)

   def testTrigProblem(self):
      self.test('Solve the equation $\\tan(2 \\theta) = 1.158$ for $\\theta$.', 
         self.trigProblem, 2)

   def testTrigProblem2(self):
      self.test('Solve the equation $\\tan(2 \\theta) = -0.000$ for $\\theta$.', 
         self.trigProblem, math.pi)

   def testTrigProblem3(self):
      self.test('Solve the equation $\\tan(2 \\theta) = -0.000$ for $\\theta$.', 
         self.trigProblem, math.pi/2)

   def testTrigProblem3(self):
      self.test('Determine whether 0.785 is in the domain of the function $f(\\theta) = \\tan(2 \\theta)$.', 
         self.trigProblem, math.pi/4)

   def testTrigProblem4(self):
      self.test('Determine whether -8.639 is in the domain of the function $f(\\theta) = \\tan(2 \\theta)$.', 
         self.trigProblem, math.pi/4 - 3*math.pi)

