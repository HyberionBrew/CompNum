# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:32:14 2019

@author: Fabian Kresse
"""

import numpy as np

count = 0
tries = 10000
x = tries
while x != 0:
    x = x - 1
    ar = np.array([i for i in range(0,100)])
    np.random.shuffle(ar)
    for i in range(0,100):
        if ar[i] == i:
            count = count + 1
           
            break
    
    
print("Count", count)
print("tries", tries)
print("per",1 -( count/tries))