from .testrunner import TestSuite

class Grader(TestSuite):
   def __init__(self, *modules):
      super(Grader, self).__init__()

      attrs = [
         ("ifelse", ["absoluteValue", "isLeapYear", "singlesAmountTaxed", "frogToPrince", "domainName"]), 
         ("collatz", ["collatzify", "collatzSequence", "frequency", "histogram", "collatzHistogram"]),
      ]

      for m, (moduleName, functionNames) in zip(modules, attrs):
         self.assertAttributesExist(m, *functionNames)
         for fName in functionNames:
            setattr(self, fName, getattr(m, fName))

   
   def testAbsolute1(self):
      self.test(0, self.absoluteValue, 0)
   
   def testAbsolute2(self):
      self.test(5, self.absoluteValue, -5)

   def testAbsolute3(self):
      self.test(144, self.absoluteValue, 144)

   def testIsLeapYear1(self):
      self.test(True, self.isLeapYear, 4)

   def testIsLeapYear2(self):
      self.test(True, self.isLeapYear, 2000)

   def testIsLeapYear3(self):
      self.test(False, self.isLeapYear, 2100)

   def testSinglesAmountTaxed1(self):
      self.test(10.0, self.singlesAmountTaxed, 100)

   def testSinglesAmountTaxed2(self):
      self.test(4500.0, self.singlesAmountTaxed, 30000)

   def testSinglesAmountTaxed3(self):
      self.test(21950.0, self.singlesAmountTaxed, 87800)

   def testSinglesAmountTaxed4(self):
      self.test(24598.280000000002, self.singlesAmountTaxed, 87851, floatComparison=True)

   def testSinglesAmountTaxed5(self):
      self.test(131455.5, self.singlesAmountTaxed, 398350)

   def testSinglesAmountTaxed6(self):
      self.test(140000.0, self.singlesAmountTaxed, 400000)

   def testSinglesAmountTaxed7(self):
      self.test(396000.0, self.singlesAmountTaxed, 1000000)

   def testFrog1(self):
      self.test('My kingdom for a frog!', self.frogToPrince, '')

   def testFrog2(self):
      self.test('Frog prince Frog schmince!', self.frogToPrince, 'Frog frog Frog schmince!')

   def testFrog3(self):
      self.test('You want me to kiss a prince?', self.frogToPrince, 'You want me to kiss a frog?')

   def testFrog4(self):
      self.test('My kingdom for a frog!', self.frogToPrince, 'Frogs are icky.')

   def testDomain1(self):
      self.test('', self.domainName, 'herp derp.')

   def testDomain2(self):
      self.test('uic.edu', self.domainName, 'doctorwho@uic.edu')

   def testDomain3(self):
      self.test('herp.derp', self.domainName, 'ermagerd@herp.derp')

   def testDomain4(self):
      self.test('', self.domainName, 
                '1234567890!#$%^&*()~`asdfghjkl;":{}?><|qwertyuiop[]zxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,./')

   def testCollatzify1(self):
      self.test(0, self.collatzify, 0)
   
   def testCollatzify2(self):
      self.test(4, self.collatzify, 1)
   
   def testCollatzify3(self):
      self.test(14, self.collatzify, 28)

   def testCollatzify4(self):
      self.test(46, self.collatzify, 15)

   def testCollatzSequence1(self):
      self.test([1], self.collatzSequence, 1)

   def testCollatzSequence2(self):
      self.test([16,8,4,2,1], self.collatzSequence, 16)

   def testCollatzSequence3(self):
      self.test([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], self.collatzSequence, 7)

   def testCollatzSequence4(self):
      self.test([657, 1972, 986, 493, 1480, 740, 370, 185, 556, 278, 139, 418, 209, 628, 314, 157, 472, 236, 118, 59, 178, 89, 268, 134, 67, 202, 101, 304, 152, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], self.collatzSequence, 657)

   def testFrequency1(self):
      self.test(0, self.frequency, 5, [1,2,3,4])

   def testFrequency2(self):
      self.test(2, self.frequency, 5, [1,5,3,4,5])

   def testFrequency3(self):
      self.test(5, self.frequency, -6, [-6,-6,-6,-6,-6,-7])

   def testFrequency4(self):
      self.test(0, self.frequency, 1, [])

   def testHistogram1(self):
      self.test([0,3,3,3], self.histogram, [1,1,1,2,2,2,3,3,3])

   def testHistogram2(self):
      self.test([1,1,1,1,1,1,1,1,1,1], self.histogram, range(10))

   def testHistogram3(self):
      self.test([1,2,2,0,1,0,1,3,1,1,0,0,0,0,0,0,0,0,0,1], self.histogram, [6,4,2,8,7,7,9,0,1,1,2,7,19])

   def testHistogram4(self):
      self.test([0]*25 + [1], self.histogram, [25])

   def testCollatzHistogram4(self):
      self.test([0, 1, 1], self.collatzHistogram, 2)

   def testCollatzHistogram1(self):
      self.test([0, 1, 1, 1, 0, 0, 1, 0, 1], self.collatzHistogram, 5)

   def testCollatzHistogram2(self):
      self.test([0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], self.collatzHistogram, 10)

   def testCollatzHistogram3(self):
      self.test([0, 1, 1, 1, 1, 1, 2, 2, 4, 4, 6, 5, 7, 9, 8, 12, 17, 12, 16, 9, 15, 22, 11, 18, 22, 14, 23, 9, 17, 30, 10, 23, 6, 13, 25, 7, 14, 22, 8, 16, 4, 10, 22, 7, 15, 3, 9, 21, 5, 11, 15, 4, 10, 3, 8, 15, 3, 8, 0, 3, 10, 1, 5, 0, 1, 7, 1, 2, 4, 2, 6, 2, 3, 6, 1, 3, 0, 1, 3, 1, 2, 1, 2, 3, 1, 2, 6, 2, 5, 2, 3, 6, 2, 4, 3, 3, 7, 2, 5, 10, 2, 5, 2, 4, 7, 4, 6, 4, 6, 8, 5, 7, 6, 7, 10, 4, 7, 14, 6, 11, 4, 8, 14, 4, 9, 1, 5, 11, 2, 6, 15, 1, 7, 0, 3, 9, 0, 2, 0, 0, 3, 0, 2, 5, 1, 4, 0, 0, 5, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], self.collatzHistogram, 1000)
