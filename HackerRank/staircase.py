#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a = (n - 1) * ' ' + '#'
    for i in range(n):
        print(a)
        a = a[1:] + '#'

if __name__ == '__main__':
    n = int(input())

    staircase(n)
