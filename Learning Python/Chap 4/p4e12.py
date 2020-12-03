# -*- coding: utf-8 -*-
"""
Exercise 12 of the Part IV of the book "Learning Python"
Four tipes of functions to solve factorials and usage of timeit module
Created on Mon Nov  9 17:06:23 2020

@author: lfbia
"""

import math, timeit
from functools import reduce

X = 70

def usingmath():
    return math.factorial(X)

def usingsimplecounter():
    X0 = 1
    counter = 1
    while counter <= X:
        X0 *= counter
        counter += 1
    return X0

def usingrecursive1(X): 
    if X > 1:
        X *= usingrecursive1(X - 1)
    return X

def wrapper(func, *args, **kwargs):
    def usingrecursive():
        return func(*args, **kwargs)
    return usingrecursive

wrapped = wrapper(usingrecursive1, 70) # using a wrapper to time with timeit
    
def usingreduce():
    return reduce(lambda x, y: x * y, range(X, 0, -1), 1)



tests = (usingmath, usingsimplecounter, wrapped, usingreduce)
for test in tests:
    time = timeit.timeit(test, number = 100000)
    print("%-20s clocked: %-20s seconds" % (test.__name__, time))