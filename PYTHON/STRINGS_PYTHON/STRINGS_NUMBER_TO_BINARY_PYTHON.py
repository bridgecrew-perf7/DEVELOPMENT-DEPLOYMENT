#!/usr/bin/env python3

# problem: input int needs conversion to bin
# solution: convert num to bin with bin()

input = 221

def num_bin(num):
    binary = bin(num)
    return binary

print(num_bin(input))
