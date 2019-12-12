# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:08:09 2019

@author: Fabian Kresse
"""
import numpy as np
import matplotlib.pyplot as plt

iterations = 15
def comp_f_dx(x):
    f = np.zeros((3,3))
    f[0][0] = 3
    f[0][1] =np.sin(x[2]*x[1])*x[2]
    f[0][2] =np.sin(x[1]*x[2])*x[1]
    f[1][0] = 8* x[0]
    f[1][1] = -1250 *x[1]
    f[1][2] = 2
    f[2][0] = np.e**(-x[0]*x[1]) * (-x[1])
    f[2][1] = np.e**(-x[0]*x[1]) * (-x[0])
    f[2][2] = 20
    return f    
    
def comp_f(x):
    f = np.zeros((3,1))
    f[0] = 3 *x[0] -np.cos(x[1]*x[2]) - (3/2)
    f[1] = 4 *x[0]**2 - 625*x[1]**2 + 2 *x[2] -1
    f[2] = 20 *x[2] + np.e**(-x[0]*x[1]) +9
    return f

x = np.array([[1],[1],[1]])

error = np.zeros((iterations))

for i in range(0,iterations):
    x_e = x
    f = comp_f(x)
    f_dx = comp_f_dx(x)
    #as ax=b
    delta = np.linalg.solve(f_dx,f)
    x = x - delta
    error[i] = np.linalg.norm(x - x_e)
    #print(x)
print(x)
print(error)

x_axis = np.linspace(0,iterations-1,iterations)+1
plt.semilogy(x_axis, error,"ro",label ='error estimate')
plt.semilogy(x_axis, np.e**-x_axis,"r",label ='O(n)')
plt.semilogy(x_axis, np.e**(-x_axis*2),"b",label ='O(n**2)')
plt.semilogy(x_axis, np.e**(-x_axis*3),"g",label ='O(n**3)')