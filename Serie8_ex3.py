# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:16:21 2019

@author: Fabian Kresse
"""
import numpy as np

N = np.array([2**i for i in range(2,11)])
for n in N:
    sampl = np.random.uniform(low=-1/n, high=1/n, size=(n,))
    b = np.zeros(n)
    A = np.zeros((n,2))
    A[:,0] = sampl
    A[:,1] = sampl**3
    b = np.sin(sampl)
    a = (A.T@A)
    b = A.T@b
    x = np.linalg.solve(a,b)
    print(x)
    
