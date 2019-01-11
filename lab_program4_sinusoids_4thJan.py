#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:44:35 2019

@author: rgukt
"""


import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,0.1,100)
f=200
fs=500
y=np.sin(2*np.pi*f*x)
plt.plot(x,y)
plt.show()
z=np.sin(2*np.pi*fs*x)
plt.plot(x,z)
plt.show()
