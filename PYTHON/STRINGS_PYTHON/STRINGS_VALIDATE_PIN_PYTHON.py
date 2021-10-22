#!/usr/bin/env python3

# problem: validate input string by certain criteria
# solution: validate string with function: isnumeric and len

input = "0000"

def validate(pin):
    return input.isnumeric() and len(input) in [4, 6]

print(validate(input))
