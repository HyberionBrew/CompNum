# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:40:20 2019

@author: fabian
"""

import numpy as np
x = [0,1,4]
y = [0,2,8]
p = np.polyfit(x,y,2)
z = np.polyval(p,2)
print(p)
print(z)