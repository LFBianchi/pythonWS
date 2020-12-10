#!/bin/python3

import math
import os
import random
import re
import sys

a = [[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0], 
     [0, 0, 2, 4, 4, 0], 
     [0, 0, 0, 2, 0, 0], 
     [0, 0, 1, 2, 4, 0]]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = []
    for j in range(1, 5):
        for i in range(1, 5):
            result.append(sum(arr[j-1][i-1:i+2]) + arr[j][i] + sum(arr[j+1][i-1:i+2]))
    return max(result)      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
