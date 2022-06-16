#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given all numbers between 1,2,…,n except one. Your task
is to find the missing number.
"""

number = int(input("Enter an integer n: "))

numbers = [int(i) for i in input("Enter numbers: ").split(" ")]

for i in range(number):
    j = i + 1
    if not j in numbers:
        print(j)
        break

### Gauss sum

total_sum = sum(numbers)
gauss_sum = number * (number + 1) / 2
print(int(gauss_sum - total_sum))