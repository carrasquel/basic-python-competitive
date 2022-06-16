#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reverse a Python string
"""

phrase = input("Enter a pharse: ")

output = ""
i = len(phrase) - 1

while i >= 0:

    output += phrase[i]
    i -= 1

print(output)