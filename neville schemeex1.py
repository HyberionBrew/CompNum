# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:47:13 2019

@author: fabian
"""
import numpy as np
import matplotlib.pyplot as p
import matplotlib
#x = [0,1,4]
#f = [0,2,8]

#1.2
class Neville:
    """
        Returns a matrix that has been build according to the
        Neville-scheme
    """
    def __init__(self,x,f):
        self.x = x
        self.f = f
        self.neville = np.zeros((len(x),len(x)),dtype = np.poly1d)
        for i in range(0,len(x)):
            self.neville[i,0]= np.poly1d(f[i])
            
    def calc(self):
        x = self.x
        neville = self.neville
        for column in range(1,len(x)):
            for row in range(0,len(x)-column):
                p1 = (np.poly1d([1,0],variable = 'x')- x[row])* neville[row+1,column-1]
                p2 = (np.poly1d([1,0],variable = 'x') -x[row+column]) *neville[row,column-1]
                neville[row,column] = ((p1 -p2) / (x[row+column]-x[row]))
        #print(neville)
        #print(neville[0][len(x)-1])
        return neville

#1.3
f = []
h = []
h.append(0)
f.append(1)
for i in range(1,11):
    h.append((2**(-i)))
    f.append((np.exp(h[i])-1)/h[i])

N = Neville(h,f)
matrix = N.calc()
c = []
for col in range(0,3):
    x = []
    for row in range(0,11):
        if (matrix[row][col] != 0):
            z = matrix[row][col](0)
        else :
            z = 0
        x.append(z)
    c.append(x)
   
p.loglog(h,c[0],'bo')
p.loglog(h,c[1],'ro')
p.loglog(h,c[2],'yo')
p.gca().invert_xaxis()
p.ylabel('abs-error')

