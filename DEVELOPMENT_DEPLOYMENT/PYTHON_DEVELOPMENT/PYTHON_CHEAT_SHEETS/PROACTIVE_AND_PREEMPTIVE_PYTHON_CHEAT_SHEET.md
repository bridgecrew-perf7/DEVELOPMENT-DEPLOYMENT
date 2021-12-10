# Proactive and Preemptive Python Cheat Sheet

_LINT, DOCUMENT, HANDLE, LOG, TEST & DEBUG LIKE A PRO_  
_Proactive Python Example: Make easy debugging likely_  
_Preemptive Python Example: Make user churn due to bugs unlikely_  

## Lint for PEP, Use Python typing
```
sudo apt install pylint
```
## Documentation best practices, Git best practices, Documentation generators
```
```
## Omnipresent Exception error handling, Exception error printing
list of all built in exceptions
```
Exception
StopIteration
SystemExit
StandardError
ArithmeticError
OverflowError
FloatingPointError
ZeroDivisionError
AssertionError
AttributeError
EOFError
ImportError
KeyboardInterrupt
LookupError
IndexError
KeyError
NameError
UnboundLocalError
EnvironmentError
IOError
OSError
SyntaxError
IndentationError
SystemError
SystemExit
TypeError
ValueError
RuntimeError
NotImplementedError
```
use exception filter like
```
try:
    print("string")

except Exception as e:
    print(traceback.format_exc())
    print(str(e))

except TimeoutException as te:
    print(te)
finally:
    return "string"
```
## Extensive Logging
```
```
## Business logic tests, Unit tests, Test driven development
```
1 Business Logic Test = 1 Test Action
A rrange
A ct
A ssert
```
## Python code debugging with Python modules and Linux commands
_use prints to divide and conquer, zoom in on the troublemaker in locality (where in the code) and concept (where in the processing of the code). make it transparent_
```
print(f"before function xyz - {dict}")
print(f"inside function xyz - {dict}")
print(f"after function xyz - {dict}")
find / -name '*.py' -exec grep -l "keyword" {} \;
grep -iaR
history | grep
du
find
dir()
data()
