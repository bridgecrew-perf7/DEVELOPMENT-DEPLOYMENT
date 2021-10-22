#!/usr/bin/env python3

# problem: input mood string needs evaluation
# solution: if input string (bool), return string, else mood neutral

mood = ""

def statement(mood):
    return "I feel {} today!".format(mood)

if bool(mood):
    print(statement(mood))
else:
    print(statement(mood="neutral"))
