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
        self.neville_sym = np.zeros((len(x),len(x)),dtype = np.poly1d)
        for i in range(0,len(x)):
            self.neville[i,0]= np.poly1d(f[i])
            self.neville_sym[i,0]= np.poly1d(f[i])
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
    def calc_sym(self,h):
        x = self.x
        neville_sym = self.neville_sym
        for column in range(1,len(x)):
            for row in range(0,len(x)-column): #row = i #colum = j
                neville_sym[row,column] = neville_sym[row+1][column-1] - (h[row+column]**2 /((h[row+column]**2)- (h[row]**2)))* (neville_sym[row+1,column-1] - neville_sym[row][column-1])
        return neville_sym
        

#1.3
def plot(h,c):
    
    p.loglog(h,c[0],'bo',label='Col 0')
    p.loglog(h,c[1],'ro',label='Col 1')
    p.loglog(h,c[2],'yo',label='Col 2')
    p.loglog(h, [i**2  for i in h], 'r', label ='O(n^2)')
    p.loglog(h, [i**3  for i in h], 'b',label ='O(n^3)')
    p.loglog(h, [i**4  for i in h], 'y',label ='O(n^4)')
    #p.ylim(0.1,3)
    
    p.legend()
    p.gca().invert_xaxis()
    p.ylabel('error')
    p.xlabel('h')

def tan_fc():
    f = []
    h = []
    for i in range(0,11):
        h.append((2**(-i)))
        f.append((np.tan(h[i])-np.tan(-h[i]))/ (2*h[i]))
    return h,f

def max_fc():
    f = []
    h = []
    for i in range(0,11):
        h.append((2**(-i)))
        f.append((max(h[i],0)**(3/2))/ (2*h[i]))
        
    return h,f

def ex2_max():
   
    h,f = tan_fc()
    #h,f = max_fc()
    N = Neville(h,f)
    matrix = N.calc_sym(h)
    c = []
    for col in range(0,3):
        x = []
        for row in range(0,11):

            if (matrix[row][col] != 0):
                #change error_max to 1 for ex 2
                z = abs(matrix[row][col](0)-1)
            else :
                z = 0
            x.append(z)
            #print(z)
        c.append(x)
    plot(h,c)    
    
def ex1_max():
    h,f = tan_fc()
    #h,f = max_fc()
    N = Neville(h,f)
    matrix = N.calc()
    c = []
    
    for col in range(0,3):
        x = []
        for row in range(0,11):

            if (matrix[row][col] != 0):
               
                z = abs(matrix[row][col](0)-1)
            else :
                z = 0
            x.append(z)
            #print(z)
        c.append(x)
    plot(h,c)
    

#ex1()
ex1_max()
#ex2_max()