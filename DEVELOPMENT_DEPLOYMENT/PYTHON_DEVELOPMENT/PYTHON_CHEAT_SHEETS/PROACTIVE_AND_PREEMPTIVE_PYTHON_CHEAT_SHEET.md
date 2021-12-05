# Proactive and Preemptive Python Cheat Sheet

_LINT, DOCUMENT, HANDLE, LOG, TEST & DEBUG LIKE A PRO_  
_Proactive Python Example: Make easy debugging likely_  
_Preemptive Python Example: Make security breach unlikely_  
_Use https://explainshell.com/_  

## Lint for PEP!
```
sudo apt install pylint
```
## Generate Documentation!
```
```
## Omnipresent Exception Handling!
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
## Extensive Logging!
```
```
## Real life Automation Testing!
```
```
## Python Debugging with Python Modules and Linux commands!
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
