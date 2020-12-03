# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:12:12 2020

From 'Learning Python'
updatedb.py
"""
import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()