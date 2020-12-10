#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print(sum(heapq.nsmallest(4, arr)), sum(heapq.nlargest(4, arr)))

    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
