#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    null = [ x for x in arr if x == 0]
    print(len(pos) / len(arr))
    print(len(neg) / len(arr))
    print(len(null) / len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
