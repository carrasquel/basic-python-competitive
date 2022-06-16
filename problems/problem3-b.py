#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program that reads a list of non-negative numbers from
the standard input, with one number per line, and prints a
histogram corresponding to those numbers. In this histogram,
each number N is represented by a vertical line of N characters "#"
"""

integers_str = input("Enter non-negative positive integers: ")

integers = [int(i) for i in integers_str.split(" ")]
lines = list()
max_value = max(integers)

for integer in integers:

    line = integer * "#" + (max_value - integer) * " "
    lines.append(line)

for j in range(max_value-1, -1, -1):
    line = ""
    for i in range(len(lines)):
        line += lines[i][j]
    print(line)
