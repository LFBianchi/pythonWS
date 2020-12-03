# -*- coding: utf-8 -*-
"""
Exercise 10 of the Part IV of the book "Learning Python"
Timing three ways to get the square root of a number
Created on Mon Nov  9 16:12:52 2020

@author: lfbia
"""

#Modified from file timeseqs.py
#Test the relative speed of iteration tool alternatives.

import sys, math, timer1 as timer # Import timer functions
reps = 10000
repslist = list(range(reps)) # Hoist out, list in both 2.X/3.X

def usingmath():
    return [math.sqrt(x) for x in repslist]

def usingasterisk():
    return [x**.5 for x in repslist]

def usingpow():
    return [pow(x, .5) for x in repslist]

print(sys.version)
for test in (usingmath, usingasterisk, usingpow):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
