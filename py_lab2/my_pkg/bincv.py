#!/usr/bin/python
import sys

stack = []

def hexnum(hex_num):
    if(hex_num < 10):
        if(hex_num <= 0):
            print('',end='')
        stack.append(hex_num)
    else:
        if(hex_num == 10):
            stack.append('A')
        elif(hex_num == 11):
            stack.append('B')
        elif(hex_num == 12):
            stack.append('C')
        elif(hex_num == 13):
            stack.append('D')
        elif(hex_num == 14):
            stack.append('E')
        elif(hex_num == 15):
            stack.append('F')

def binto_oct(bin_num):
    oct_num = 0
    oct_count = count = 0
    bin_num = reversed(bin_num)
    for i, digit in enumerate(bin_num):
        oct_num += int(digit) * pow(2, count) * pow(10, oct_count)
        if(i % 3 == 2):
            oct_count += 1
            count = 0
        else:
            count += 1
    print("=> OCT>", oct_num)

def binto_dec(bin_num):
    dec_num = 0
    bin_num = reversed(bin_num)
    for i, digit in enumerate(bin_num):
        dec_num += int(digit)*pow(2, i)
    print("=> DEC>", dec_num)

def binto_hex(bin_num):
    hex_num = 0
    count = 0
    bin_num = reversed(bin_num)
    print("=> HEX> ", end='')
    for i, digit in enumerate(bin_num):
        hex_num += int(digit) * pow(2, count)
        if(i%4 == 3):
            count = 0
            hexnum(hex_num)
            hex_num = 0
        else:
            count+=1
    hexnum(hex_num)
    for i in range(0, len(stack)):
        num = stack.pop()
        if(num == 0):
            continue
        print(num, end='')
    print()
