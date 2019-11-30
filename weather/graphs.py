# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:01:08 2019

@author: Admin
"""

import matplotlib.pyplot as plt                                                 
import numpy as np
import math

## Create functions and set domain length
x = np.arange(-5.0, 5.0, 0.01)
y = x**x
z=0
## Plot functions and a point where they intersect
plt.plot(x, y)
plt.plot(x, z)
plt.plot(1, 1, 'or')

## Config the graph
plt.title('A Cool Graph')
plt.xlabel('X')
plt.ylabel('Y')
#plt.ylim([0, 4])
plt.grid(True)
plt.legend(['y = x', 'y = 2x'], loc='upper left')

## Show the graph
plt.show()