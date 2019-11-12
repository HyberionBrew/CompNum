# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 08:46:53 2019

@author: Fabian Kresse
"""
import numpy as np
u = np.zeros((40))
u[1]=2
for k in range(1,u.shape[0]-1):
   u[k+1] = 2**(k) * np.sqrt(2*(1-np.sqrt(1-(2**(-k) * u[k])**2)))

error = abs(np.pi -u)
print(error)
ind_error = np.argmin(error)
print("The error is minimal at:",ind_error , error[ind_error])

#6.4b) mostly because of representation errors , the number just cant be reprented good enough
#that is because 2**-k gets realy small and has to be therefore cut of
n = 3

x = np.zeros(20)

q_prev = 0
for n in range(1,20):
    q = (u[n+1]-u[n+2]) /(u[n]-u[n+1])
    C = (u[n]-u[n+1])/(q**(n)-q**(n+1))
    x[n] = u[n] - C* q**n
    if q > 1 or q<0:
        break
    q_prev = q**n

error = abs(np.pi -x)
ind_error = np.argmin(error)
print(error)
print("The error is minimal at:", ind_error , error[ind_error])


#6.5b) yes once q**n changes from becoming bigger and it encounters an overflow (check if q is outside of (0,1))
