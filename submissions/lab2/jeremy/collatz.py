
def collatzify(n):
   return n/2 if n % 2 == 0 else 3*n + 1


def collatzSequence(number):
   seqSoFar = [number]

   while number > 1:
      number = collatzify(number)
      seqSoFar.append(number)

   return seqSoFar


def frequency(soughtNumber, numberList):
   counter = 0

   for x in numberList:
      if x == soughtNumber:
         counter = counter + 1

   return counter


def histogram(numberList):
   # return a list of frequency counts from 0 to max(numberList)

   highest = max(numberList)
   current = 0
   theHistogram = []

   while current <= highest:
      theHistogram.append(frequency(current, numberList))
      current = current + 1

   return theHistogram


def collatzHistogram(numberOfNumbers):
   collatzLengths = []

   for n in range(1, numberOfNumbers+1):
      collatzLengths.append(len(collatzSequence(n)))

   return histogram(collatzLengths)


def printHist(aHistogram):
   import math
   theMax = max(aHistogram)
   numDigits = math.ceil(math.log10(len(aHistogram)))
   formatter = "%" + str(numDigits) + "d "

   for i, count in enumerate(aHistogram):
      print((formatter % i) + ("#" * int(round(10.0 * count / theMax))))


if __name__ == "__main__":
   from unittest import test

   test(8, collatzify(16))
   test(14, collatzify(28))
   test(10, collatzify(3))

   test([1], collatzSequence(1))
   test([5,16,8,4,2,1], collatzSequence(5))
   test([7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], collatzSequence(7))

   test(0, frequency(5,[1,2,3,4]))
   test(1, frequency(3,[1,2,3,4]))
   test(5, frequency(6,[1,6,6,6,6,7,6]))

   test([1,1,1,1,1,1,1,1,1,1], histogram(range(10)))
   test([1,2,2,0,1,0,1,3,1,1,0,0,0,0,0,0,0,0,0,1], histogram([6,4,2,8,7,7,9,0,1,1,2,7,19]))
   test([0]*25 + [1], histogram([25]))

   test([0,1,1], collatzHistogram(2))
   test([0,1,1,1,0,0,1,0,1], collatzHistogram(5))
   test([0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], collatzHistogram(10))
