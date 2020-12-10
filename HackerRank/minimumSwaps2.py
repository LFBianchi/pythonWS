#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    stepCount = 0
    hashMap = {}
    for pos, val in enumerate(arr):
        hashMap[val] = pos
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            stepCount += 1
            temp = arr[i]
            arr[i] = i + 1
            arr[hashMap[i + 1]] = temp
            
            hashMap[temp]= hashMap[i+1]
    
    return stepCount
            
        
def swapper(arr, pos1, pos2): #swaps elements from pos1 with pos 1 with a given array.
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp
    return arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
