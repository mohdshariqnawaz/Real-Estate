# A SIMPLE DEBUGGING FUNCTION FOR PYTHON PROGRAMS.
# IF THE ENVIRONMENT VARIABLE DEBUG1 IS NOT SET (AT THE
# COMMAND PROMPT, THE DEBUG1 FUNCTION DOES NOTHING.
# IF THE SAME VARIABLE IS SET TO ANY VALUE, THE
# DEBUG1 FUNCTION PRINTS THE MESSAGE AND OPTIONAL
# VALUES PASSED TO IT.
import os

if os.getenv("DEBUG1"):
     def debug1(message, *values):
         if len(values) == 0:
             print (message),
         else:
             print (message, ":"),
         for value in values:
             print (repr(value)),
         print
else:
    def debug1(message, *values):
        pass

def main(): # Test the debug1 function with some calls.
    debug1('z')
    debug1('a', 1)
    debug1('b', 1, "hi")
    debug1('c', 1, "hi", True)
    debug1('d', 1, "hi", True, [2, 3])
    debug1('d', 1, "hi", True, [2, 3], {'a': 'apple', 'b': 'banana'})

if __name__ == '__main__':
    main()
