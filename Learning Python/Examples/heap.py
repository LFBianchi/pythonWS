"""
Self implementation of the heap functionality
"""

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
