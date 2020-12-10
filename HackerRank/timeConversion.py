#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hours = int(s[:2])
    mins = int(s[3:5])
    segs = int(s[6:8])
    if s[-2:] == 'PM':
        if not hours == 12:
            hours += 12
    if s[-2:] == 'AM':
        if hours == 12:
            hours = 0
    if hours < 10:
        hours = '0' + str(hours)
    if mins < 10:
        mins = '0' + str(mins)
    if segs < 10:
        segs = '0' + str(segs)
    return str(hours) + ':' + str(mins) + ':' + str(segs)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
