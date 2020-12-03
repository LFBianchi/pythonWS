# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:55:20 2020

@author: lfbia
Trie implementation in python
Run the code for speed comparison using python
"""

class Node: 
    def __init__(self, data = None, endWord = False):
        self.data = data
        self.endWord = endWord
        
class Trie(Node):
    def include(self, word):
        """
        Includes a word in the trie
        """
        word = list(word)
        curr = self
        while word:
            letter = word.pop(0)
            if not curr.data:
                curr.data = {}
            if letter not in curr.data:
                curr.data[letter] = Node()
            curr = curr.data[letter]
        else:
            curr.endWord = True
            
    def findPartial(self, partial):
        """
        Looks for a substring of a string in the trie
        """
        flag = False
        partial = list(partial)
        curr = self
        while partial:
            letter = partial.pop(0)
            if letter not in curr.data:
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

    
if __name__ == '__main__':
    test = Trie()
    test.include('abcde')
    test.include('fghi')
    test.include('adtcte')
    test.include('adtctek')
    print(test.findPartial('abc'))
    print(test.findPartial('acd'))
    print(test.countPartial('a'))