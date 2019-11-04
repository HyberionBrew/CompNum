# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:07:52 2019

@author: fabian kresse
@brief: realizes the adaptive quadrature for an integral f(x)dx from a to b,
@details: is based on the simpson rule
"""
import numpy as np
import matplotlib.pyplot as p

def func(x):
    if x < 1/3:
        return (1/2) * np.e**x 
    else:
        return np.e**x

def simpsonRule(f,a,b):
    
    return ((b-a) /6) *(f(a) + 4*f((a+b)/2) + f(b))

def trapezoidRule(f,a,b):
    return (b-a)*(f(a)+f(b))/2   

def integralE():
    return ((np.e**1 - np.e**(1/3))) + 1/2 *(np.e**(1/3) - np.e**(0))

def adapt(f,a,b,tau,h_min):
    sim = simpsonRule(f,a,b)
    sim2 = simpsonRule(f,a,(a+b)/2) + simpsonRule(f,(a+b)/2,b)
    
    if (b-a) <= h_min: 
        return sim2
    
    if (abs(sim-sim2)<= tau):
        return sim2
    
    else:
        m = (a+b)/2
        x1 = adapt(f,a,m,tau,h_min)
        x2 = adapt(f,m,b,tau,h_min)
        value =  x1+x2 
        return value
    
h_min = [1/(2**i) for i in range(0,20)]
error = []
for h in h_min:       
    x = adapt(func,0,1,h,h)
    error.append(abs(x - integralE()))
    
p.figure(0)
p.loglog(h_min,error,'bo',label='Error')
p.loglog(h_min,h_min,'r',label='O(n)') 
p.legend()
p.gca().invert_xaxis()
p.ylabel('error')
p.xlabel('h')
#convergenc is ~ O(n^2)
#h_min = tau because then it will always terminate in tau exept 