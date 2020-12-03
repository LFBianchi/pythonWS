# -*- coding: utf-8 -*-
"""
Exercise 5 of the Part IV of the book "Learning Python"
Function "addDict" - Returns a union of dictionaries
Created on Mon Nov  9 11:06:47 2020

@author: lfbia
"""
def addList(list1, list2):
    return list1 + list2

def addDict(aurelio, michaellis):
    D = {}
    for i in aurelio.keys():
        D[i] = aurelio[i]
    for i in michaellis.keys():
        D[i] = michaellis[i]
    return D

def addListDict(A, B):
    if type(A) == list: return addList(A, B)
    else: return addDict(A, B)

print(addListDict({'edi': 1,
                'noelia': 2,
                'anselmo': 4},
               {'nilcilene': 54,
                'arlete': 55,
                'sandra': 8}))
print(addListDict([1, 2, 3, 4, 5],
                  [5, 3, 4, 5]))
print(addListDict([5, 3, 4, 5],
                  [1, 2, 3, 4, 5]))