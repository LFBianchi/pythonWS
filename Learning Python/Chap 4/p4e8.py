# -*- coding: utf-8 -*-
"""
Exercise 8 of the Part IV of the book "Learning Python"
Function isprime: Determines if a number is a prime
Created on Mon Nov  9 12:56:40 2020

@author: lfbia
"""

def isprime(y):
    if y > 1: return isprimenum(y)
    else: 
        print("0, 1 and negatives can't be primes you dummy")
        return False

def isprimenumslow(y): #slow
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            return False
        x -= 1
    else:
        print(y, 'is prime')
        return True
    
def isprimenum(y):  # faster
    y = int(y)
    x = y // 2
    factors = [i for i in range(2, x, 1) if y % i == 0]
    if factors:
        print(y, 'has factor', max(factors))
        return False
    else:
        print(y, 'is prime')
        return True

for x in range(1, 68, 2):
    isprime(x)
    
isprime(16.0)
isprime(7.0)
isprime(0)
isprime(1)