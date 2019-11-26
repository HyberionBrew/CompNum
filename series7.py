# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 06:02:13 2019

@author: Fabian Kresse
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sci
n = 10
e = np.ones(10)[np.newaxis]
e = e.T
b = np.zeros(10)[np.newaxis]
b[0][0] = 1
b = b.T
A = 10* np.identity(10) + b * e.T + e * b.T
#print(A)
print("----------")

plt.figure(0)
plt.spy(A)
print(A)
print(sci.lu(A))
plt.figure(1)
print("------------")
#interchange rows

for i in range(0, int(A.shape[0]/2)):
    row_temp = np.copy(A[i])
    A[i] = A[A.shape[0]-i-1]
    A[A.shape[0]-i-1] = row_temp

for i in range(0, int(A.shape[0]/2)):
    row_temp = np.copy(A[:,i])
    A[:,i] = A[:,A.shape[0]-i-1]
    A[:,A.shape[0]-i-1] = row_temp
      
plt.spy(A)
print(sci.lu(A))
#print(A)

#observation: The first matrix needs a lot more calculations for the
#L and U matrix
#Scriptum (Skyline Matrices) - Theorem 4.23 
#Factors L, U of a skiline matrix A have the same sparsity pattern as A.