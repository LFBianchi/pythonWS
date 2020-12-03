# -*- coding: utf-8 -*-
"""
Exercise 5 of the Part IV of the book "Learning Python"
Function "copyDict" - Makes a copy of a given dictionary
Created on Mon Nov  9 11:06:47 2020

@author: lfbia
"""
def copyDict(aurelio):
    D = {}
    for i in aurelio.keys():
        D[i] = aurelio[i]
    return D

print(copyDict({'edi': 1,
                'noelia': 2,
                'anselmo': 4}))