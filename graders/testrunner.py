import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass
epsilon = 0.00000000001
max_num_seconds = 15

@contextmanager
def time_limit(seconds=max_num_seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def withArgumentString(functionName, args):
   argstr = "when calling %r with " % (functionName,)

   if len(args) == 0:
      argstr += "no arguments."
   elif len(args) == 1:
      argstr += "the argument %r" % args[0]
   else:
      argstr += "the arguments %s" % (",".join([repr(x) for x in args]),)

   return argstr
   

def badReturnValue(actual, functionName, args):
   error = "Got incorrect return value %r " % (actual,)

   return error + withArgumentString(functionName, args)

def badReturnValueFunction(fActual, fArgs, functionName, args):
   return "The function returned by %r %s gave an incorrect return value %r for input %r" % (functionName, 
      withArgumentString(functionName, args), fActual, fArgs)


class TestSuite(object):
   def __init__(self):
      self.failures = []

   def assertAttributesExist(self, module, *attrs):
      for name in attrs:
         if not hasattr(module, name):
            moduleName = module.__name__[module.__name__.rfind(".")+1:]
            print("Submitted module %r does not have the required attribute %r" % (moduleName, name))
            exit(-1)

   def getTests(self):
      return [attr for attr in dir(self) if attr != "test" and attr.startswith("test")]

   def countTests(self):
      return len(self.getTests())

   def runTests(self):
      for f in self.getTests():
         try:
            getattr(self, f)()
         except Exception as e:
            self.failures.append("You caused a %s: %s " % (type(e).__name__, e))
            raise

      numFailures = len(self.failures)
      if numFailures == 0:
         print("All tests pass. Congratulations!")
         return 1.0
      else:
         print("You failed one or more tests. The first failing test was:")
         print(self.failures[0])
         numTests = self.countTests()
         return float(numTests - numFailures) / numTests


   def test(self, expected, function, *args, **kwargs):
      try:
         with time_limit():
            actual = function(*args) 

            if expected != actual and ('floatComparison' not in kwargs or abs(expected - actual) > epsilon):
               self.failures.append(badReturnValue(actual, function.__name__, args))

               if 'callback' in kwargs:
                  kwargs['callback']()

      except TimeoutException:
         self.failures.append("Error: function call timed out. You spent more than %d seconds in the function %r when called with arguments %r" % (max_num_seconds, function.__name__, args))
      except Exception as e:
         self.failures.append("Error: %s " % (e,) + withArgumentString(function.__name__, args))


   def _testOutputFunction(self, fExpected, fArgs, function, args, **kwargs):
      try:
         with time_limit():
            f = function(*args)
            fActual = f(*fArgs)

            if fExpected != fActual and ('floatComparison' not in kwargs or abs(fExpected - fActual) > epsilon):
               self.failures.append(badReturnValueFunction(fActual, fArgs, function.__name__, args))

               if 'callback' in kwargs:
                  kwargs['callback']()

      except TimeoutException:
         self.failures.append("Error: function call timed out. You spent more than %d seconds in the function %r when called with arguments %r" % (max_num_seconds, function.__name__, args))
      except Exception as e:
         self.failures.append("Error: %s " % (e,) + withArgumentString(function.__name__, args))

   def _testValue(self, expected, actual):
      if expected != actual:
         self.failures.append("Expected %r but got %r" % (expected, actual))

