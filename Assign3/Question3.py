# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:13:19 2022

@author: kevin
"""
import cv2
import skimage.io as io
import numpy as np

img = cv2.imread('car.png')
#io.imshow(img) # original image

sobelX = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobelY = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)
sobelXY = cv2.Sobel(sobelX, cv2.CV_64F,0,1,ksize=5)
#io.imshow(sobelX) 
#io.imshow(sobelY) 
io.imshow(sobelXY)
