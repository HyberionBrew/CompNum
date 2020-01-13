# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:01:50 2020

@author: Fabian Kresse
"""
import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt
#a)
epsilon = 10**-14

def QR(A,lmax):
    X = np.identity(A.shape[0])
    l = 0
    Q,R = np.linalg.qr(X)
    #print(Q,R)
    result = []
    while l < lmax:
        #old A and Q
        Q, R = np.linalg.qr(A)
        #new Q and R
        A = R@Q
        l = l +1
        result.append(np.diagonal(A))
        #print(np.diagonal(X))
    return result 


def QR_Wilkinson(A):
    eig = []
    A = linalg.hessenberg(A)
    QR_steps = 0
    for i in range(A.shape[0],0,-1):
        k  = 0
        while ((abs(A[i-2,i-1]) > epsilon* (abs(A[i-2,i-1]+A[i-1,i-1])))):
            k = k + 1
            if k > 1000:
                print("Endless")
                break
            A_u = A[i-2:i,i-2:i]
            ew, ev = np.linalg.eig(A_u)
            
            if (abs(ew[0]-A_u[1,1])>abs(ew[1]-A_u[1,1])):
                k = ew[1]
            else:
                k = ew[0]
            A = A - np.identity(A.shape[0])*k
            Q, R = np.linalg.qr(A)
            QR_steps = QR_steps +1
            A = R@Q + np.identity(A.shape[0])*k
        eig.append(A[i-1,i-1])
        
    return eig, QR_steps

A = np.array([[1,3,4],[3,1,2],[4,2,1]])
ew, ev = np.linalg.eig(A)
print("EW laut np: ", ew)
eig = QR(A,10)
print("EW laut QR: ", eig[-1])
#b
eig, steps = QR_Wilkinson(A)
print("EW laut QR-shift (steps): ", eig, steps)
#c
max_iter = 1000
i = 0
plt.figure(0)
for j in [2**3,2**5]:
    n = j
    A = np.diag([2]*n)
    A = A + np.diag([-1]*(n-1),k=1) + np.diag([-1]*(n-1),k=-1)
    ew, ev = np.linalg.eig(A)
    ew = np.sort(ew)
    
    eig_w = QR(A,max_iter)
    eig_w = np.sort(eig_w,axis = 1)
    error = np.linalg.norm(eig_w-ew,axis = 1)
    x_axis = np.linspace(0,max_iter-1,max_iter)
    #plt.figure(i)
    if i == 1: 
        plt.semilogy(x_axis, error,"ro",label ='1')
    else:
        plt.semilogy(x_axis, error,"bo",label ='0')
    i = i +1
plt.legend()

#d
plt.figure(1)

max_iter = 100
i = 0

iterations = []
for j in range(2,10):
    n = 2**j
    print(n)
    A = np.diag([2]*n)
    A = A + np.diag([-1]*(n-1),k=1) + np.diag([-1]*(n-1),k=-1)
    ew, ev = np.linalg.eig(A)
    ew = np.sort(ew)
    
    eig_w = QR(A,max_iter)
    eig_w = np.sort(eig_w,axis = 1)
    error = np.linalg.norm(eig_w-ew,axis = 1)
    x_axis = np.linspace(0,max_iter-1,max_iter)
    #plt.figure(i)
    for i in range(0, max_iter):
        if error[i] < 10**-2 or i == max_iter-1:
            iterations.append(i)
            break

print(iterations)
x_axis = np.linspace(0,iterations[-1]-1,iterations[-1])
plt.loglog([2**i for i in range(2,len(iterations)+2)],iterations,"ro")
#plt.legend()

