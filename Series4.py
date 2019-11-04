# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:58:51 2019

@author: fabian
"""

import numpy as np
#import Neville-Scheme
from neville_scheme_ex1 import Neville
import matplotlib.pyplot as p

#for the Romberg extrapolation
def calc_function_points(a,b,i,func):
    h = (b-a)/(2**i)
    f_values = np.zeros(((2**i)+1))
    for x in range(0,(2**i) +1):
        f_values[x] = func(a)
        a = a + h
    return f_values

def calc_trapezoid(a,b,func_points,h):
    if len(func_points) > 2:
        sum_trap = sum(func_points[1:-1])*h  + (func_points[0] + func_points[-1])*(h/2)
        return sum_trap
    else:
        return (func_points[0] + func_points[-1])/2



def fnc_1(x):
    return x**0.2
def fnc_1_dx():
    return 5/6
def fnc_3_dx():
    return 1/3

def fnc_2(x):
    return x**10
def fnc_2_dx():
    return 1/11
def fnc_3(x):
    return x**2

a = 0
b = 1
i = 3

def RombergIntegration(a,b,func,func_dx):
    alpha = 10#stepsize
    h = np.zeros(alpha)
    trap = np.zeros(alpha)
    for i in range(0,alpha):
        h[i] = (b-a)* (2**-i)
        fnc_points = calc_function_points(a,b,i,func)
        trap[i] = calc_trapezoid(a,b,fnc_points,h[i])
    #neville auf die trapezregel angewandt
    nev = Neville(h**2,trap)
    matrix = nev.calc()
    #auswertung bei h = 0
    error = []
    for i in range(0,3):
        x = []
        for row in range(0,alpha):
            if (matrix[row][i] != 0):
                z = abs(matrix[row][i](0) - func_dx())
            else :
                z = 0
            x.append(z)
        error.append(x)
    return error,h


#annäherung des Integrals über trapezsummen
#h_i -> i =  0...alpha
for fnc in range(0,3):
    if fnc == 0:
        error,h = RombergIntegration(a,b,fnc_1,fnc_1_dx)    
    elif fnc == 1:
        error,h = RombergIntegration(a,b,fnc_2,fnc_2_dx)  
    else:
        error,h = RombergIntegration(a,b,fnc_3,fnc_3_dx)  
    p.figure(fnc)
    p.loglog(h,error[0],'bo',label='Col 0')
    p.loglog(h,h,'b')
    p.loglog(h,h**2,'b')
    p.loglog(h,h**4,'b')
    p.loglog(h,error[1],'ro',label='Col 1')
    p.loglog(h,error[2],'yo',label='Col 2')
    p.ylim((-100,100))
    p.legend()
    p.gca().invert_xaxis()
    p.ylabel('error')
    p.xlabel('h')

