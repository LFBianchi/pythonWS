# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 07:54:11 2020

From Learning Python
makedb.py

"""
from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

