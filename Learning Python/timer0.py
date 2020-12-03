# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:19:41 2020

@author: lfbia
"""

import time
def timer(func, *args):
    start = time.perf_counter()
    for i in range(1000):
        func(*args)
    return time.perf_counter() - start