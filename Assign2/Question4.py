# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:49:05 2022

@author: kevin
"""
from numpy.fft import * 
f = [2,3,4,1]
ff = fft(f)
for x in ff:
    print ("%0.4f %+0.4fi" % (x.real, x.imag))