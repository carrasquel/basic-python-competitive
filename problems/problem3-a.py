#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a program that reads a list of non-negative numbers from
the standard input, with one number per line, and prints a
histogram corresponding to those numbers. In this histogram,
each number N is represented by a line of N characters "#"
"""

integers_str = input("Enter non-negative positive integers: ")

integers = [int(i) for i in integers_str.split(" ")]

for integer in integers:

    print(integer * "#")