# -*- coding: utf-8 -*-
"""
Exercise 10 of the Part IV of the book "Learning Python"
Timing three ways to get the sqr root of a number, modified for dictionaries
Created on Mon Nov  9 16:12:52 2020

@author: lfbia
"""

#Modified from file timeseqs.py
#Test the relative speed of iteration tool alternatives.

import sys, timer1 as timer # Import timer functions
reps = 10000
repslist = list(range(reps)) # Hoist out, list in both 2.X/3.X

keys = list('abcdefgh')
values = [1, 2, 3, 4, 5, 6, 7, 8]

def dictcomp():
    return {keys[i]: values[i] for i in range(8)}

def dictfor():
    dictionary = {}
    for i in range(8):
        dictionary[keys[i]] = values[i]
    return dictionary


print(sys.version)
for test in (dictcomp, dictfor):
    total, result = timer.total(100000, test)
    print ('%-9s: %s' %
           (test.__name__, total))
