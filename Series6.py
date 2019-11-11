# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:50:50 2019

@author: Fabian Kresse
"""
#6.2
import matplotlib.pyplot as p

def func_1(x,y):
    return x**2

def func_2(x,y):
    return 2

def func_3(x,y):
    if x < y:
        return 0
    else:
        return 1
    
def midpoint_rule(f,x,y):
    return (x[1]-x[0]) * (y[1]-y[0]) * f((x[0]+x[1])/2,(y[0]+y[1])/2)
    
def adapt(f,x,y,tau,h_min):
    """
    @brief adaptive quadrature in 2d
    """

    mid = midpoint_rule(f,x,y)
    
    new_midpoint_x = (x[1]+x[0])/2
    new_midpoint_y = (y[1]+y[0])/2
    mid2 = midpoint_rule(f,(x[0],new_midpoint_x),(y[0],new_midpoint_y)) + \
           midpoint_rule(f,(x[0],new_midpoint_x),(new_midpoint_y,y[1])) + \
           midpoint_rule(f,(new_midpoint_x,x[1]),(y[0],new_midpoint_y))+ \
           midpoint_rule(f,(new_midpoint_x,x[1]),(new_midpoint_y,y[1]))
    
    if (x[1]-x[0]) <= h_min:
        return mid2
    
    if (abs(mid-mid2)<= tau):
        return mid2
    
    else:

        x1 = adapt(f,(x[0],new_midpoint_x),(y[0],new_midpoint_y),tau,h_min)
        x2 = adapt(f,(x[0],new_midpoint_x),(new_midpoint_y,y[1]),tau,h_min)
        x3 = adapt(f,(new_midpoint_x,x[1]),(y[0],new_midpoint_y),tau,h_min)
        x4 = adapt(f,(new_midpoint_x,x[1]),(new_midpoint_y,y[1]),tau,h_min)
        value =  x1+x2+x3+x4
        return value

#tau_h = 0.01
#value = adapt(func_1,(0,1),(0,1),tau_h,tau_h)
#print(value)

h_min = [1/(2**i) for i in range(0,30)]
error = []
error2 = []

for h in h_min:       
    x = adapt(func_1,(0,1),(0,1),h,h)
    #print(x)
    error.append(abs(x - 1/3))
i = 0
for h in h_min:       
    x2 = adapt(func_3,(0,1),(0,1),h,h)
    print(i)
    i = i +1
    error2.append(abs(x2 - 1/2))
    
p.figure(0)
p.loglog(h_min,error,'bo',label='Error for x**2')
p.loglog(h_min,error2,'yo',label='Error for fc2')
p.loglog(h_min,h_min,'r',label='O(n)') 
p.legend()
p.gca().invert_xaxis()
p.ylabel('error')
p.xlabel('h')