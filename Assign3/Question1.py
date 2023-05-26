# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:58:16 2022

@author: kevin
"""
import cv2
import skimage.io as io
import numpy as np
from skimage.morphology import binary_dilation as bwdilate
from skimage.morphology import binary_erosion as bwerode
from skimage.morphology import closing, opening, binary_closing as bwclose, binary_opening as bwopen

b1 = np.array([[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0],[0,0,0,1,1,1,1,0],
               [0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,0,0,0],
               [0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0]])
b2 = np.array([[0,1,0],[1,1,1],[0,1,0]])

print(b1)
print(b2)

be = bwerode(b1,b2) # erosion
#io.imshow(be)

bd = bwdilate(b1,b2) # dilation
#io.imshow(bd)

bo = bwopen(b1,b2)
#io.imshow(bo)

bc = bwclose(b1,b2)
#io.imshow(bc)