#!/usr/bin/python

import sys
import my_pkg

while(True):
    select = int(input("Select menu : 1) conversion 2) union/intersection 3) exit   "))
    if (select == 1):
        binstr = input("input binary number : ")
        my_pkg.binto_oct(binstr)
        my_pkg.binto_dec(binstr)
        my_pkg.binto_hex(binstr)
    elif(select == 2):
        my_pkg.unioninter()
    elif(select == 3):
        break

print("exit the program...")
sys.exit()
