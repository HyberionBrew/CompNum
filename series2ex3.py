# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:37:57 2019

@author: fabian
"""
import numpy as np
import time
#2.3
def calculateSum(N):
    su = 0
    for i in range(1,N+1):
        su = su + 1/i
    return su

def calculateSum2(N):
    su = 0
    for i in range(1,N+1):
        su = su + 1/(i**2)
    return su
def approx(N,a):
    return np.log(N) + a[0] + a[1]/N + a[2]/(N**2)

def compare(N,a):
    start = time.time()
    ap = approx(N,a)
    print("approx ran: ", time.time()-start)
    
    start = time.time()
    cal = calculateSum(N)
    print("cal ran: ", time.time()-start)
    error = cal - ap
    print(error)
    
def matrix_row(N):
    return np.array([1/N,1/(N**2)])

b = np.zeros((3,1))

b[0] = calculateSum(10) - np.log(10)
b[1] = calculateSum(100)- np.log(100)
b[2] = calculateSum(1000)- np.log(1000)

X = np.ones((3,3))
#for i in [1,2,3]:
 #   X[]
print("2.4")
X[0,1] = 1/10
X[0,2] = 1/100

X[1,1] = 1/100
X[1,2] = (1/100)**2

X[1,1] = 1/1000
X[1,2] = (1/1000)**2

a = np.linalg.solve(X,b)
#error for 10**6
#compare(10**6,a)
#compare(10**8,a) #10s


b[0] = calculateSum2(10)
b[1] = calculateSum2(1000)
b[2] = calculateSum2(100000)

#print(b)
X = np.ones((3,3))
X[0,1:] = matrix_row(10)
X[1,1:] = matrix_row(1000)
X[2,1:] = matrix_row(100000)
#print(X)

a = np.linalg.solve(X,b)
#10s
print(a[0]-((np.pi**2)/6))


