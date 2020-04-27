#!/usr/bin/python
import sys
import re

def unioninter():
    unionset = []
    interset = []
    a = input("1st list : ")
    a = re.sub('[^0-9]', ' ', a)
    a = list(a.split())
    b = input("2nd list : ")
    b = re.sub('[^0-9]', ' ', b)
    b = list(b.split())

    a = list(map(int, a))
    b = list(map(int, b))
    for i in a:
        if i in b:
            interset.append(i)
    for i in a:
        if not i in unionset:
            unionset.append(i)
    for i in b:
        if not i in unionset:
            unionset.append(i)
    unionset.sort()
    interset.sort()
    print("=> union "+str(unionset))
    print("=> intersection "+str(interset))



