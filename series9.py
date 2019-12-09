# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:30:53 2019

@author: Fabian Kresse
"""
import numpy as np
import matplotlib.pyplot as plt

def function1(x):
    return x**2
def func1_dx(x):
    return 2*x

def function2(x):
    return (np.e**x) -2

def function2_dx(x):
    return (np.e**x)

def func3(x):
    return abs(x)**(3/2)

def func3_dx(x):
    if x == 0:
        return 0
    else:
        return (3*x)/(2*np.sqrt(abs(x)))

def func4(x):
    return (1/x)-1

def func4_dx(x):
    return -(1/(x**2))

def newton(x,f,df):
    return x - (f(x)/df(x))

results = np.zeros((4,20))

x = np.zeros((4,1))+2.1
for i in range(0,results.shape[1]):
    x[0] = newton(x[0],function1,func1_dx)
    results[0][i] = x[0]
    
    x[1] = newton(x[1],function2,function2_dx)
    results[1][i] = x[1]
    
    x[2] = newton(x[2],func3,func3_dx)
    results[2][i] = x[2]
    
    x[3] = newton(x[3],func4,func4_dx)
    results[3][i] = x[3]
    
error = results
error[0] = results[0]-0
error[1] = results[1]-np.log(2)
error[2] = results[2]-0
error[3] = results[3]-1

print(error[3])
x_axis = np.linspace(0,results.shape[1]-1,results.shape[1])+1
plt.semilogy(x_axis, np.e**-x_axis,"r",label ='O(n)')
plt.semilogy(x_axis, np.e**(-x_axis*2),"b",label ='O(n*2)')
plt.semilogy(x_axis, error[0],"ro",label ='fnc_1')
plt.semilogy(x_axis, error[1],"go",label ='fnc_2')
plt.semilogy(x_axis, error[2],"bo",label ='fnc_3')
plt.semilogy(x_axis, error[3],"yo",label ='fnc_4')

plt.legend()
plt.show()
#print(error)