#!/usr/bin/env python3

# problem: date input string is off local normative
# solution: split and join string to comply with local normative

input = "11/22/1992"

def format_date(date):
    m, d, y = date.split('/')
    return ''.join((y, d, m))

print(format_date(input))
