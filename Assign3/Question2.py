# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:12:11 2022

@author: kevin
"""
import cv2
import skimage.io as io
import numpy as np

c = io.imread("circles.png").astype('bool')*1
#io.imshow(c) # original image
x = np.random.random_sample(c.shape)
c[np.nonzero(x>0.95)] = 0
c[np.nonzero(x<=0.05)] = 1

#io.imshow(c) # original image with noise
c = c.astype('uint8')
opening = cv2.morphologyEx(c, cv2.MORPH_OPEN, np.ones((2,2),np.uint8))
#io.imshow(opening) # half of final result
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, np.ones((2,2),np.uint8))
io.imshow(closing) # final result
