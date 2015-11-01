from datetime import date

deadlines = {'lab0': date(2017, 1, 1),
             'lab1': date(2015, 11, 1),
             'lab2': date(2015, 11, 7),
             }

projectModules = {'lab0': ("lab0",),
                  'lab1': ("lab1",), 
                  'lab2': ("ifelse", "collatz"),
                  }

def isLate(project):
   return (date.today() - deadlines[project]).days > 0

