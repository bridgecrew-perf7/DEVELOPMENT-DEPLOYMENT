#!/usr/bin/env python3

def M(n, x, y):

    ycount = 1
    for p in range(n):
        print(". ", end = "")

        xcount = 1
        for l in range(n):
            replace = "."
            if x == xcount and y == ycount:
                replace = ("o")
            print(replace, end = " ")

            xcount += 1
        print()
        ycount +=1

print(M(8, 4, 3))
