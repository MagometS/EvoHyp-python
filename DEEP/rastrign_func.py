#!/usr/bin/env python3  
import sys
from math import pi, cos


def rastrign_func(xx : list):
    sum = 0
    for x in xx:
        sum += x ** 2 - 10 * cos(2 * pi * x)

    return len(xx) * 10 + sum


xx = list()

for i in sys.argv[1:]:
    xx.append(float(i))

print(rastrign_func(xx))
