#Solution for HackerRank problem using cpython heapq module
#!/bin/python3

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
    print(runningMedian([1, 2, 3, 4]),
          runningMedian([1, 2, 3]),
          runningMedian([1, 2]),
          runningMedian([1]))
    a = []
    b = []
    for line in open('tcase1.txt'):
        a.append(int(line))
    a.pop(0)
    for line in open('tcase1ans.txt'):
        b.append(float(line.rstrip()))
    c = runningMedian(a)
    print(b == c)
