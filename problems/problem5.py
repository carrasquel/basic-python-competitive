#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sequence of integers A, a maximal identical sequence is
a sequence of adjacent identical values of maximal length k. Write
a program that reads an input sequence A, with one or more
numbers per line, and outputs the value of the first (leftmost)
maximal identical sequence in A.
"""

from pyrsistent import m


numbers = [int(i) for i in input("Enter a sequence of numbers: ").split(" ")]
# numbers = list(map(int, input.split()))

numbers = numbers[::-1]

most = 1
search = most
prev = numbers[0]

for next in numbers[1:]:

    if next == prev:
        search += 1
    else:
        prev = next
        if search > most:
            most = search
        search = 1

print(most)
