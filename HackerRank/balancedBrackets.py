#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
dictBrackets = {'[': ']', '(': ')', '{': '}'}
openers = '([{'


def isBalanced(s):
    stackBrackets = []
    Flag = True
    for x in s:
        if x in openers:
            stackBrackets.append(x)
        else:
            if stackBrackets:
                if dictBrackets[stackBrackets[-1]] == x:
                    stackBrackets.pop(-1)
                else: 
                    Flag = False
                    break            
            else:
                Flag = False
                break
    if stackBrackets: Flag = False
    
    return 'YES' if Flag else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
