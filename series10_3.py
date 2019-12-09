# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:48:08 2019

@author: Fabian Kresse
"""
import numpy as np

epsilon = 0.01
iterations = 100

def comp_f(X,eps):
    f = np.zeros((2,1))
    f[0] = 2*X[0] + X[1] - eps * (X[0]-X[1])**2
    f[1] = X[0] + 2*X[1] - eps*3
    return f

def comp_f_dx(X,eps):
    f = np.zeros((2,2))
    f[0][0] = 2 - eps * (X[0]-X[1])* 2 * -X[1]
    f[0][1] = 1 - eps * (X[0]-X[1])* 2 * X[0]
    f[1][0] = 1
    f[1][1] = 2
    return f

x = np.zeros((2,1))
A = np.array([[2,1],[1,2]])
b = np.array([[0],[3]])

x_0 = np.linalg.solve(A,b)

error = np.zeros((2,iterations))
x = x_0

for i in range(0,iterations):
    x_e = x
    f = comp_f(x,epsilon)
    f_dx = comp_f_dx(x,epsilon)
    delta = np.linalg.solve(f_dx,f)
    x = x - delta
    error[0][i] = np.linalg.norm(x - x_e)
x_solution = x
    
def f_exc(X):
    f = np.zeros((2,1))
    f[0] = (X[0]-X[1])**2
    return f
    

x = x_0
print(x)
for i in range(0, iterations):
    b_n = b + epsilon * f_exc(x)
    x = np.linalg.inv(A) @ b_n
    #x = np.linalg.solve(A,b_n)
    print(x)
    error[1][i] = np.linalg.norm(x - x_solution)
    
print(error)