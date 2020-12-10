#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    counter = 0
    aset = set(a); bset = set(b)
    a = {i: a.count(i) for i in aset}
    b = {i: b.count(i) for i in bset}
    for i in a.keys():
        if b.get(i, False):
            if b[i] != a[i]:
                counter += abs(b[i] - a[i])
        else:
            counter += a[i]
    for i in b.keys():
        if not a.get(i, False):
            counter += b[i]
            
    return counter
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
