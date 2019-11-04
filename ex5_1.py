#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:57:40 2019

@author: fabian
"""
import numpy as np

def function_1(x):
    #for a)
    return x**2

def composite_gaus(n,L,q):
    x = np.linspace(0,1,3)
    y= np.array([function_1(i) for i in x])
    legr = np.polynomial.legendre.legfit(x,y,2)
    print(legr.leggaus(n))

composite_gaus(2,1,1)