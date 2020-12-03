# -*- coding: utf-8 -*-
"""
Exercise 11 of the Part IV of the book "Learning Python"
Simple recursive function usage
Function recursive: counts down to zero from the integer passed in.
Created on Mon Nov  9 16:47:51 2020

@author: lfbia
"""

def recursive(I):
    print(I, end= ' ')
    if I > 0:
        recursive(I - 1)
    else:
        print('')
        
recursive(5)
recursive(10)
recursive(15)


#extra: generator function
def recursivegen(I):
    I += 1
    while I > 0:
        I -= 1
        yield I