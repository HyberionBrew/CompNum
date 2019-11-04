#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:57:40 2019

@author: fabian
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def f_1(x):
    return x**2
def f_2(x):
    return x**1
def f_3(x):
    return x**0
def f(x):
    return (x**0.1) * np.log(x)

f_result = 0.82644 

def composite_gaus(f,n,L,q):
    result = 0
    a = 0
    b = 1
    intervals = np.zeros(L+1)
    intervals[1:] = np.array([q**i for i in range(L-1,-1,-1)])
    x,w = np.polynomial.legendre.leggauss(n)
    #translate to interval n[i] n[i+1]
    for i in range(0,len(intervals)-1 ):
        a = intervals[i]
        b = intervals[i+1]
        new_x = 0.5 *(x+1)*(b-a) +a 
        result = result + sum(w*f(new_x)) * 0.5 * (b-a)
    return result

#ex a)
print("x**2")
print(composite_gaus(f_1,10,10,0.5))
print("x**1")
print(composite_gaus(f_2,10,10,0.5))
print("x**0")
print(composite_gaus(f_3,10,10,0.5))
#ex b)
error = np.zeros((3,19))
q_c = 0
all_L = np.array([i for i in range(1,20)])

for q in [0.5,0.15,0.05]:
    for L in all_L:
        error[q_c][L-1] =  abs(composite_gaus(f,L,L,q) + f_result)
    q_c += 1

plt.semilogy(all_L, error[0],"ro",label ='q= 0.5')
plt.semilogy(all_L, error[1],"yo",label ='q= 0.15')
plt.semilogy(all_L, error[2],"go",label ='q= 0.05')
#plt.semilogy(all_L, np.log(error[2]),"y",label ='e')


pole1 = np.polyfit(all_L, np.log(error[0]),1)
print(np.e**(pole1[0]),"*","e**(",pole1[1],"x)")
pole1 = np.polyfit(all_L, np.log(error[1]),1)
print(np.e**(pole1[0]),"*","e**(",pole1[1],"x)")
pole1 = np.polyfit(all_L, np.log(error[2]),1)
print(np.e**(pole1[0]),"*","e**(",pole1[1],"x)")