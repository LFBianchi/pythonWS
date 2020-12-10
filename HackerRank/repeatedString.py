#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    result = 0    
    asForString = s.count('a')
    lenString = len(s)
    
    result += (n // lenString) * asForString
    if n % lenString:
        result += s[:n % lenString].count('a')
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
