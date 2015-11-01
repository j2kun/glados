from .testrunner import TestSuite

class Grader(TestSuite):
   def __init__(self, *modules):
      super(Grader, self).__init__()

      (m,) = modules
      self.expectedModules = ["identity"]
      self.assertAttributesExist(m, *self.expectedModules)

      for fName in self.expectedModules:
         setattr(self, fName, getattr(m, fName))
   
   def testIdentity1(self):
      self.test(1, self.identity, 1)

   def testIdentity2(self):
      self.test("hello", self.identity, "hello")

