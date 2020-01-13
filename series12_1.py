# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:45:42 2020

@author: Fabian Kresse
"""

import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return 2-x**2-np.e**x

def F_dx(x):
    return -2*x-np.e**x

def calcP(xArr, xfin):
    erg = np.zeros(len(xArr))
    for i in range(0,len(xArr)-1):        
        erg[i] = np.log(abs(xArr[i+1]-xfin))/np.log(abs(xArr[i]-xfin))
    return erg
    
x = 2.5
x_new = 1

xNewton = np.zeros(8)
#1
i = 0
while abs(x-x_new) > 10**-12:
    x = x_new
    x_new = x - F(x)/F_dx(x)
    xNewton[i] = x_new
    i = i +1
xNewtonfin = x_new

#2
x = 2.5
x_1 = x - F(x)/F_dx(x)

H = 1
s = x_1 - x
y = F(x_1)-F(x)
H = H + (1/(abs(s)**2))*(y-H*s)*s

x_old = x
x_new = x_1
xSekant = []
#while abs(x_old-x_new)>10**-12:
for i in range(0,8):
    s = x_new - x_old
    y = F(x_new)-F(x_old)
    H = H + (1/(abs(s)**2))*(y-H*s)*s
    x_old = x_new
    x_new = x_new - 1/H *F(x_new)
    xSekant.append(x_new)

error = np.array(xSekant)- xNewtonfin
error_Newton = np.array(xNewton)- xNewtonfin
x_axis = np.linspace(0,7,8)
conv_order = calcP(xSekant,xNewtonfin)



plt.figure(0)
plt.semilogy(x_axis, error,"ro",label ='Secant')
plt.legend()
plt.figure(1)
plt.plot(x_axis, conv_order,"go",label ='conv_order')
#almost quadratic convergence
plt.legend()
plt.figure(2)
print(error_Newton)
plt.semilogy(x_axis*3, error_Newton,"go",label ='Error Newton')
plt.semilogy(x_axis*3, error,"ro",label ='Error Secant')
plt.legend()





















