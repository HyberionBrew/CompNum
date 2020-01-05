# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:44:58 2020

@author: Fabian Kresse
"""
import numpy as np
import matplotlib.pyplot as plt

def Rayleight(A,x):
    return (x.T@A@x)/(x.T@x)

def Rayleight_grad(A,x):
    quo = 2 * ((A@x*np.linalg.norm(x)**2) -(x.T@A@x)*x) 
    
    div = np.linalg.norm(x)**4
    return (quo)/div

q = 0.5
sigma = 0.5
error = []

n = 10

for n in [10,20,40,80]:
    h = 1/n
    
    A = np.diag([2]*n)
    A = A + np.diag([-1]*(n-1),k=1) + np.diag([-1]*(n-1),k=-1)
    A = 1/(h**2) * A
    x = np.array([np.random.rand(n)]).T
    w,v = np.linalg.eig(A)
    all_Eigen = []
    
    
    for i in range(100):
        R_g = Rayleight_grad(A,x)
        descend = -R_g
        R = Rayleight(A,x)
        all_Eigen.append(R[0][0])
        if (R_g.T@descend > 0):
            print("No descend possible")
            break
        
        foundK = False
        k = 0
        while not(foundK):
            if (Rayleight(A,x+(q**k)*descend)< R + sigma*(R_g.T@descend)*q**k):
                step_size = q**k
                foundK = True
            elif Rayleight(A,x+(q**k)*descend)== R + sigma*(R_g.T@descend)*q**k:
                step_size = q**k
                foundK = True
            k = k + 1
        x = x + step_size * descend
        
    error.append(abs(all_Eigen-w[0]))
    
    
x_axis = np.linspace(0,99,100)
plt.semilogy(x_axis, error[0],"ro",label ='n = 10')
plt.semilogy(x_axis, error[1],"go",label ='n = 20')
plt.semilogy(x_axis, error[2],"bo",label ='n = 40')
plt.semilogy(x_axis, error[3],"yo",label ='n = 80')
plt.legend()




