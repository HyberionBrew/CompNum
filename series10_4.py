# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:21:55 2019

@author: Fabian Kresse
"""
import numpy as np
import matplotlib.pyplot as plt
# first go for Ax = b
N = 5
h = 1/N

#create f(x)
f = np.zeros((N,N))
column = 0

#calculate  f(x)
def calc_f(u):
    result = np.zeros((u.shape[0]))
    for i in range(0,u.shape[0]):
        if i == 0:
            result[i] = ((2*u[i]-u[i+1])/ h**2) * u[i]**3 - 1
        elif i == u.shape[0]-1:
            result[i] = ((2*u[i]-u[i-1])/ h**2) * u[i]**3 - 1
        else:
            result[i] = ((-u[i+1]+2*u[i]-u[i-1])/ h**2) * u[i]**3 - 1
            
    return result
        
def calc_f_dx(u):
    f_dx =  np.zeros((u.shape[0], u.shape[0]))
    for i in range(0,u.shape[0]):
        if i == 0:
            f_dx[i][i:i+2] = [(2/(h**2)) + 3*u[i]**2, -u[i+1]]
        elif i == u.shape[0]-1:
            f_dx[i][i-1:i+1] = [-u[i-1], (2/(h**2)) + 3*u[i]**2]
        else:
            f_dx[i][i-1:i+2] = [-u[i+1], (2/(h**2)) + 3*u[i]**2, -u[i-1]]
        #dia[i][i]=u[i]*2
    return f_dx

u = np.zeros((N))
u.fill(0.5)    
iterations = 10
error = np.zeros((iterations))
for i in range(0,iterations): 
    u_e = u
    f = calc_f(u)
    f_dx = calc_f_dx(u)
    u = np.linalg.solve(f_dx,f)
    error[i] = np.linalg.norm(u - u_e)
print(error)
#print(u)
x_axis = np.linspace(0,iterations-1,iterations)+1
plt.semilogy(x_axis, error,"ro",label ='error estimate')
plt.semilogy(x_axis, np.e**-x_axis,"r",label ='O(n)')
plt.semilogy(x_axis, np.e**(-x_axis*2),"b",label ='O(n**2)')
plt.semilogy(x_axis, np.e**(-x_axis*4),"g",label ='O(n**5)')
