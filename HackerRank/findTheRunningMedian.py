#!/bin/python3

import os
import sys
import heapq

  
def runningMedian(a):
    results = []
    mins = []
    maxs = []
    subj = None
    for num in a:
        if not subj:
            if not mins and not maxs:
                results.append(float(num))
                mins.append(- num)
                continue
            elif not maxs:
                if num > -mins[0]:
                    maxs.append(num)
                else:
                    maxs.append(- mins.pop(0))
                    mins.append(- num)
                results.append((- mins[0] + maxs[0]) / 2)
                continue
            else:
                if num > - mins[0] and num < maxs[0]:
                    subj = num
                elif num > - mins[0]:
                    subj = heapq.heappushpop(maxs, num)
                else:
                    subj = - heapq.heappushpop(mins, - num)
            results.append(float(subj))
        else:
            if num > subj:
                heapq.heappush(maxs, num)
                heapq.heappush(mins, - subj)
            else:
                heapq.heappush(mins, - num)
                heapq.heappush(maxs, subj)
            subj = None
            results.append((- mins[0] + maxs[0]) / 2)
                
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(lambda x: '%.1f' % x, result)))
    fptr.write('\n')

    fptr.close()
