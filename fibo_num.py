#!/usr/bin/python
import sys

def fibonacci(n) : 
    f1, f2 =0, 1
    temp = 0
    if(n<=1):
        return n
    elif(n>=2):
        for i in range(0, n):
            temp=f2
            f2=f1+f2
            f1=temp
            print( temp,end=' ')
    print('\n',end='')
    print("F%d=%d"%(n, temp))

a=int(input('fibonacci number?'))
fibonacci(a)

