# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:56:54 2020

@author: Fabian Kresse
"""
#11.3
import numpy as np

def power_method(A,x0):
    
    lam = x0.T@A@x0
    print("lam",lam)
    x0 = x0/ np.linalg.norm(x0)
    l = 0
    while True:
        lam_prev = lam
        x0 = A@x0
        x0_norm = np.linalg.norm(x0)
        x0 = x0/x0_norm
        lam = x0.T@A@x0
        print(lam)
        l = l +1        
        if abs(lam_prev-lam) < 10**-3:
            break
    print("----------")
    print("eigenwert",lam,"eigenvektor",x0,"Anzahl an Iterationen",l)
    return lam,x0,l

A = np.array([[2,0],[0,-2]])
x0 = np.array([[1],[0]])
x1 = np.array([[0],[1]])
x2 = np.array([[1],[1]])

power_method(A,x0)
#doesnt convrge to the same eigenvalue, because both have same magnitude
power_method(A,x1)
#A has no eigenvalue that is strictly greater in magnitude than its other eigenvalues, 
#because of the x2 doesnt converge to an eigenvalue
power_method(A,x2)


