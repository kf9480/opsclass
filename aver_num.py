#!/usr/bin/python
import sys

_sum = 0
n = int(input('Number of input : '))
for i in range(0, n):
    num = int(input('input number : '))
    _sum += num;

avg = _sum / n
print('average : ', avg)
