# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:24:05 2020

@author: Fabian Kresse
"""

#Continuation Method
import numpy as np
x = 4
def H(x,s):
    return np.arctan(x)-(1-s)*np.arctan(4)

def H_dx(x):
    return 1/(x**2+1) 

i = np.array([i for i in range(1,11)])

s = i/10
for si in s:
    x = x - H(x,si)/H_dx(x)
    print(x)