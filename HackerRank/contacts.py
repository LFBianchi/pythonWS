#!/bin/python3

import os
import sys

class Node:
    def __init__(self, data = None, endWord = False):
        self.data = data
        self.endWord = endWord
        
class Trie(Node):            
    def include(self, word):
        """
        Includes a word in the trie
        """
        curr = self
        for letter in word:
            if not curr.data:
                curr.data = {}
            if not curr.data.get(letter, None):
                curr.data[letter] = Trie()
            curr = curr.data[letter]
        else:
            curr.endWord = True
            
    def findPartial(self, partial):
        """
        Looks for a substring of a string in the trie
        """
        flag = False
        curr = self
        for letter in partial:
            if not curr.data:
                break
            if not curr.data.get(letter, None):
                break
            curr = curr.data[letter]
        else:
            flag = True
            
        return (flag, curr) if flag else (flag, None)
    
    def countPartial(self, partial):
        """
        Counts the number of strings that contain a substring
        """
        find = self.findPartial(partial)
        count = 0
        if find[0]:
            queue = [find[1]]
            while queue:
                curr = queue.pop(0)
                if curr.data:
                    for i in curr.data.values():
                        queue.append(i)
                if curr.endWord == True:
                    count += 1            
            
        return count


def contacts(queries):
    contactList = Trie()
    result = []
    for pair in queries:
        if pair[0] == 'add':
            contactList.include(pair[1])
        else:
            result.append(contactList.countPartial(pair[1]))
    
    return result
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
