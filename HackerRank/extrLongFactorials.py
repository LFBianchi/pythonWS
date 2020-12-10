#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
        
    return prod

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
