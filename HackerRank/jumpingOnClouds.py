#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    answer  = []
    possibleNodes = [i for i in range(n) if c[i] == 0]
    while possibleNodes:
        answer.append(possibleNodes[0])
        if possibleNodes[1:]:
            if possibleNodes[2:]:
                if possibleNodes[2] - possibleNodes[0] == 2:
                    possibleNodes.pop(0)
            possibleNodes.pop(0)
        else:
            possibleNodes.pop(0)
    return len(answer[1:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
