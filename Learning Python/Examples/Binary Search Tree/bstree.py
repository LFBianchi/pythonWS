# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:17:19 2020

@author: lfbia
Binary Search Tree implementation example in python, translated from C++ from:
http://cslibrary.stanford.edu/110/BinaryTrees.html
Run the code for speed comparison using timeit
"""
import timeit
class Node:
    """
    Initiates a node in a Binary Search Tree
    """
    def __init__(self, data = None, nLeft = None, nRight = None):
        self.data = data
        self.left = nLeft
        self.right = nRight

    def __repr__(self):
        return 'Data: %s' % (self.data)

class BSTree(Node):
    def callNode(self, target):     #Width search
        """
        Searches the binary tree for a given value using while. 
        Returns True or False.
        """
        if self.data == None:
            return False
        else:
            nodeQueue = [self]
            while nodeQueue:
                subject = nodeQueue.pop(0)
                if subject.data == target:
                    return True
                else:
                    nodeQueue += [i for i in
                                  (subject.left, subject.right)
                                  if i]
            else:
                return False

    def callNodeR(self, target):    #Depth search
        """
        Searches the binary tree bellow a node for a given value
        using a recursive function. Returns True of False.
        """
        if self == None:
            return False
        else:
            if self == target:
                return True
            else:
                return max(self.left.callNodeR(target),
                       self.right.callNodeR(target))

    def insert(self, data):
        """
        Adds data to the BST by width
        """
        if self.data == None:
            self.data = data
        else:
            nodeQueue = [self]
            while nodeQueue:
                subject = nodeQueue.pop(0)
                if not subject.left:
                    subject.left = BSTree(data)
                elif not subject.right:
                    subject.right = BSTree(data)
                else:
                    nodeQueue += [subject.left, subject.right]


if __name__ == '__main__':
    test = BSTree()
    print(test)
    print(test.callNode('edi'))
    for i in range(10):
        test.insert(i)
    test.insert('edi')
    timeit.timeit("test.callNode('edi')")
