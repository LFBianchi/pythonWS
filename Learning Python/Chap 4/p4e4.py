# -*- coding: utf-8 -*-
"""
Exercise 4 of the Part IV of the book "Learning Python"
Function "adder"
Created on Mon Nov  9 11:06:47 2020

@author: lfbia
"""
def adder(**kargs):
    try: S = list(kargs.values())[0][:0]
    except: S = 0
    
    for i in sorted(kargs.keys()):
        S += kargs[i]
    return S
        
print(adder(edi= 1,
            noelia= 2,
            anselmo= 4))
print(adder(aedi= 's',
            bnoelia= 'p',
            canselmo= 'am',
            dsandra= 'ing'))