# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:57:59 2019

@author: fabian
"""

import numpy as np
import matplotlib.pyplot as plt

def function_3_1(x):
    return 1/(4-(x**2))

max_degree = 100
degree_points = [i for i in range(0,max_degree)]
uniform_dist = np.linspace(-1,1,100)
error = np.zeros((max_degree))
value_fnc = np.asarray([function_3_1(i) for i in uniform_dist])
for degree in range(0,max_degree): 
    cheb = np.polynomial.Chebyshev.interpolate(function_3_1,degree)

    value_cheb = np.asarray([np.polynomial.chebyshev.chebval(i,cheb.coef) for i in uniform_dist])
    error[degree] = max(abs(value_fnc-value_cheb))

print("Excercise 3.1") 
plt.figure(0)
plt.semilogy(degree_points,error,"ro")
plt.figure(1)

print("Excercise 3.3")

def function1(x):
    return x**2

def function2(x):
    return abs(x)

def function3(x):
    if x < (1/3):
        return (1/2)*np.e**x
    else:
        return np.e**x

def integralE():
    return -1 * ((1/2)* ((np.e**-1) -np.e**(1/3)) + np. e**(1/3) - np.e)

def calc_function_points(N,h,func):
    position = -1
    f_values = np.zeros((N+1))
    for i in range(0,N+1):
        f_values[i] = func(position)
        position = position + h
    return f_values

def calc_trapezoid(func_points,x_lenght):
    sum_trap = sum(func_points[1:-1])*2 + func_points[0] + func_points[-1]
    sum_trap = sum_trap *(x_lenght/2) 
    return sum_trap

h_array = [2**-i for i in range(1,21)]

function_error = np.zeros((3,20))
i = 0
for h in h_array:
    N = int(2/h)
    f1_values = calc_function_points(N,h,function1)
    f2_values = calc_function_points(N,h,function2)
    f3_values = calc_function_points(N,h,function3)
    function_error[0][i] = abs((2/3) - calc_trapezoid(f1_values,h))
    function_error[1][i] = abs(1 - calc_trapezoid(f2_values,h))
    function_error[2][i] = abs(integralE() - calc_trapezoid(f3_values,h))
    i += 1
plt.loglog(h_array, function_error[0],"ro")
plt.loglog(h_array, function_error[2],"yo")
plt.loglog(h_array, function_error[1],"go")

print(function_error)
#print(function_error)
