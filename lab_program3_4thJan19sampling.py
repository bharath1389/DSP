#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:30:00 2019

@author: rgukt
"""

import numpy as np
import matplotlib.pyplot as plt

f=input("enter f:")
fs=input("enter fs:")
f=float(f)
fs=float(fs)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
n1=np.linspace(0,10,20)
n2=np.linspace(0,10,2000)
x=np.sin(2*np.pi*f*n2)
y=np.sin(2*np.pi*(f/fs)*n1)
ax1.plot(n2,x)
ax2.stem(n1,y)
plt.show()

