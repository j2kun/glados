# Glados

A simple CLI grading robot for an introductory python class

## Project setup

To set up a project, run 

./create_project.sh PROJECT_NAME

and this will set up the submissions directories and add it to the list of open
assignments. Then add the due date to the dictionary of deadlines in
project-info.py, and add the names of the expected submitted modules to the
list of projectModules in the same file. 

The project name is expected to be a module available for importing inside
the graders module. e.g. if the project is called project3, there should be
a file graders/project3.py and the grade.py program will try to import the
module graders.project3

The imported module is expected to have a class called Grader which extends
the TestSuite class contained in testrunner.py. Alternatively, you need not
extend TestSuite and instead craft a custom runTests() function.

runTests() should accept no arguments and return the score as a decimal
in [0,1]

## Other

More to come, should I ever decide to document this thing

