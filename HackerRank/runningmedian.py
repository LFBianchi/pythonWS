#Solution for HackerRank problem using heap
#!/bin/python3

import random

class MinHeap:
    #left = i * 2
    #right = i * 2 + 1
    #parent = i //2

    heap = [None]
    def add(self, number):
        self.heap.append(number)
        if len(self.heap) > 2:
            idx = len(self.heap) - 1
            while self.heap[idx] < self.heap[idx // 2]:
                temp = self.heap[idx // 2]
                self.heap[idx // 2] = self.heap[idx]
                self.heap[idx] = temp
                if (idx // 2) > 1:
                    idx = idx // 2

    def pop(self):
        if len(self.heap) > 1:
            result = self.heap[1]
        else:
            return None
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        if len(self.heap) > 2:
            idx = 1
            while True:
                left = idx * 2
                right = idx * 2 + 1
                if right <= (len(self.heap) - 1) and self.heap[1] > min((self.heap[left], self.heap[right])):
                    if self.heap[left] < self.heap[right]:
                        self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                        idx = left
                    elif self.heap[left] > self.heap[right]:
                        self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                        idx = right
                elif left <= (len(self.heap) - 1) and self.heap[1] > self.heap[left]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    idx = left
                else:
                    break
        return result

class MaxHeap:
    #left = i * 2
    #right = i * 2 + 1
    #parent = i //2

    heap = [None]
    def add(self, number):
        self.heap.append(number)
        if len(self.heap) > 2:
            idx = len(self.heap) - 1
            while self.heap[idx] > self.heap[idx // 2]:
                temp = self.heap[idx // 2]
                self.heap[idx // 2] = self.heap[idx]
                self.heap[idx] = temp
                if (idx // 2) > 1:
                    idx = idx // 2

    def pop(self):
        if len(self.heap) > 1:
            result = self.heap[1]
        else:
            return None
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        if len(self.heap) > 2:
            idx = 1
            while True:
                left = idx * 2
                right = idx * 2 + 1
                if right <= (len(self.heap) - 1) and self.heap[1] < max((self.heap[left], self.heap[right])):
                    if self.heap[left] > self.heap[right]:
                        self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                        idx = left
                    elif self.heap[left] < self.heap[right]:
                        self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                        idx = right
                elif left <= (len(self.heap) - 1) and self.heap[1] < self.heap[left]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    idx = left
                else:
                    break
        return result
    
def runningMedian(a):
    results = []
    numbers = sorted(a[:3])
    otherNumbers = a[3:]
    if len(a) >= 1:   
        results.append(float(a[0]))
    if len(a) >= 2:
        results.append((a[0] + a[1]) / 2)
    if len(a) >= 3:
        results.append(float(numbers[1]))
    
    if otherNumbers:
        mins = MaxHeap()
        mins.add(numbers[0])
        maxs = MinHeap()
        maxs.add(numbers[2])
        subj = numbers[1]
        for num in otherNumbers:
            if subj:
                if num > subj:
                    maxs.add(num)
                    mins.add(subj)
                else:
                    mins.add(num)
                    maxs.add(subj)
                results.append((mins.heap[1] + maxs.heap[1]) / 2)
                subj = None
            else:
                if num < mins.heap[1]:
                    mins.add(num)
                    subj = mins.pop()
                elif num > maxs.heap[1]:
                    maxs.add(num)
                    subj = maxs.pop()
                else:
                    subj = num
                results.append(float(subj))
        
    return results

if __name__ == '__main__':
    print(runningMedian([2, 3]))
    print(runningMedian([4]))
    print(runningMedian([3, 4, 9]))
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(200000):
        a.append(random.randint(1, 10 ** 6))
    print(runningMedian(a))