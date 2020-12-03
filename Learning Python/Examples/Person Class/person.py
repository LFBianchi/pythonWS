# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:32:14 2020

@author: lfbia

Person.py

Record and process information about people.

Following an Example of larger scale class from 'Learning Python' using two
classes and the shelve method.

Run this file to test its classes
"""
from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Create and process person records
    """    
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

#   New __repr__ inherited from AttrDisplay       
#   def __repr__(self):
#       return '[Person: %s, %s]' % (self.name, self.pay)
        
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        
class Manager(Person):
    """
    Customized person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
        
    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)
    
if __name__ == '__main__':  #Self test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'dev', 100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(bob)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom)