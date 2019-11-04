# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:47:13 2019

@author: fabian
"""
import numpy as np
import matplotlib.pyplot as p
x = [0,1,4]
f = [0,2,8]
#email: David.Woergoetter@tuwien.ac.at
#>60%
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
        return neville
    

#1.3
ex1 = Neville(x,f)
matrix = ex1.calc()
print(matrix)
print(matrix[0][2])

def ex2():
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
                z = abs(matrix[row][col](0) -1)
            else :
                z = 0
            x.append(z)
        c.append(x)

    p.loglog(h,c[0],'bo',label='Col 0')
    p.loglog(h,c[1],'ro',label='Col 1')
    p.loglog(h,c[2],'yo',label='Col 2')
    p.ylim((-100,100))
    p.legend()
    p.gca().invert_xaxis()
    p.ylabel('error')
    p.xlabel('h')
    
#ex2()
