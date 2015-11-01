import os
import sys
from config import BASE_DIR

finalGrades = {}
assignment = sys.argv[-1]
gradesDir = '%s/grades/' % BASE_DIR

for filename in os.listdir(gradesDir):
   if assignment not in filename:
      continue

   hyphen = filename.index('-')
   txt = filename.index('.txt')
   id = filename[hyphen+1:txt]

   with open(gradesDir + filename) as gradeFile:
      for line in gradeFile:
         tokens = line.strip().split()
   
         if len(tokens) == 2:
            tokens.append('x')
         _, score, date = tokens

         score = float(score)

         if id not in finalGrades:
            finalGrades[id] = score
         else:
            finalGrades[id] = max([finalGrades[id], score])

for key in sorted(finalGrades.keys()):
   print("%s\t%s" % (key, finalGrades[key]))
