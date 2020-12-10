#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.

"""
def checkMagazine(magazine, note):      #using dictcomp
    hashWords = {x: magazine.count(x) for x in set(note)}
    if list(hashWords.values()).count(0):
        print('No')
    else:
        hashNoteWords = {x: (hashWords[x] - note.count(x)) for x in set(note)}
        if [x for x in hashNoteWords.values() if x < 0]:
            print('No')
        else:
            print('Yes')
"""

def checkMagazine(magazine, note):
    hashWords = {}
    for word in magazine:
        if word not in hashWords:
            hashWords[word] = 0
        hashWords[word] += 1
    
    for word in note:
        if word not in hashWords:
            return 'No'
        else:
            hashWords[word] -= 1
            if hashWords[word] < 0:
                return 'No'
    else: return 'Yes'
                
            
        
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()
    
    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
