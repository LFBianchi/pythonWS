# -*- coding: utf-8 -*-
"""
Exercise 9 of the Part IV of the book "Learning Python"
Function sqrt: Determines the square root of numbers from a list
Created on Mon Nov  9 16:03:52 2020

@author: lfbia
"""

import math

def sqrt1(L):
    Lsqrt = []
    
    for x in L:
        Lsqrt.append(math.sqrt(x))
    
    return Lsqrt

def sqrt2(L):
    return list(map(math.sqrt, L))

def sqrt3(L):
    return [math.sqrt(x) for x in L]

L = [2, 4, 9, 16, 25]

print(sqrt1(L))
print(sqrt2(L))
print(sqrt3(L))