import sys
import os
from config import BASE_DIR
from projectinfo import *
from datetime import date

def updateGrades(user, project, score):
   with open('%s/grades/%s-%s.txt' % (BASE_DIR, project, user), 'a+') as gradeFile:
      gradeFile.write("%s\t%s\t%s\n" % (user, score, date.today()))

user, project = sys.argv[-2:]
print("Grading %s for user %s..." % (project, user))

# fromlist forces __import__ to return the right-most module
try:
   grader = __import__("graders.%s" % project, fromlist=['graders'])
except ImportError as e:
   print(e)
   print("You've just submitted files for %s! The test cases aren't set up yet, try again later." % (project,))
   exit()

score = 0.0
modules = []

try:
   for module in projectModules[project]: 
      modules.append(__import__("submissions.%s.%s.%s" % (project, user, module), fromlist=['submissions']))
   score = grader.Grader(*modules).runTests()

   if isLate(project):
      print("Your project is late, and will not be accepted. Sorry :(")
      score = 0

   updateGrades(user, project, score)

except ImportError as e:
   print(e)
   print("Did you submit the wrong file?")

except SyntaxError as e:
   print("Warning! You have a syntax error in your submission.\nIf you think this error is caused by the grading robot and not by your program, please contact the TA.\nAlways remember to test your code before submitting.")

except KeyError as e:
   print("It appears the submission for this project is open, but there is no grader. Chances are you are trying to submit while the TA is writing the grading robot. If you think this isn't the case, please email the TA with the following error message:")

   print("KeyError: %s" % e)
