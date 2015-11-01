def absoluteValue(x):
   if x < 0:
      return -x
   else:
      return x


def isLeapYear(year):
   if year % 100 == 0:
      return year % 400 == 0
   else:
      return year % 4 == 0


def singlesAmountTaxed(salary):
   if salary <= 8925:
      rate = 0.1
   elif salary <= 36250:
      rate = 0.15
   elif salary <= 87850:
      rate = 0.25
   elif salary <= 183250:
      rate = 0.28
   elif salary <= 398350:
      rate = 0.33
   elif salary <= 400000:
      rate = .35
   else:
      rate = 0.396

   return salary * rate


def frogToPrince(myString):
   if 'frog' in myString:
      return myString.replace('frog', 'prince')
   else:
      return 'My kingdom for a frog!'


def domainName(myString):
   # given an email address, return the domain name
   # if the input is not an email, return the empty string

   if '@' in myString:
      beginning = myString.find('@')
      return myString[beginning + 1:]
   else:
      return ''



