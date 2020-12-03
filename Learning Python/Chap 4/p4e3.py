# -*- coding: utf-8 -*-
"""
Exercise 3 of the Part IV of the book "Learning Python"
Function "adder"
Created on Mon Nov  9 11:06:47 2020

@author: lfbia
"""
def adder(*args):
    try:
        iter(args[0])
        S = args[0][:0]
        while args:
            S += args[0]
            args = args[1:]
    except:
        S = 0
        for x in args:
            S += x
    return S

print(adder('edi', 'noelia', ' anselmo'))
print(adder([1, 2], [2, 3]))
print(adder('edi'))
print(adder(1, 2, 3, 4.4))
print(adder({'edi': 1,
             'noelia': 2},
            {'anselmo': 4}))