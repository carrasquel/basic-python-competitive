#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given of input a positive integer n. If n is even, the algorithm
divides it by two, and if n is odd, the algorithm multiplies it by
three and adds one. The algorithm repeats this, until n is one.
"""

number = int(input("Enter a positive integer: "))

while number > 1:
    if number % 2 == 0:
        number /= 2
    else:
        number *= 3
        number += 1
    
    print(int(number), end=" ")