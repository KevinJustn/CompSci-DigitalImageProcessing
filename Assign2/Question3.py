# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:20:09 2022

@author: kevin
"""
import cv2
import skimage.io as io 
import skimage.util.noise as noise  
import scipy.ndimage as ndi 
img = io.imread("gull.png") 
img_20p = noise.random_noise(img, mode="s&p", amount=0.2) # 20% noise s&p

#io.imshow(img)
#io.imshow(img_20p)

#Using Average Filter - - - - - - - - - - - - - - - - - - - - - - -
avg_img20p = ndi.uniform_filter(img_20p, 3)
#io.imshow(avg_img20p)

#Using Median Filter - - - - - - - - - - - - - - - - - - - - - - -
med_img20p = ndi.median_filter(img_20p,3) #Median Filter
#io.imshow(med_img20p)

#Using Gaussian Filter - - - - - - - - - - - - - - - - - - - - - -
gau_img20p = cv2.GaussianBlur(img_20p, (5,5), 0)
#io.imshow(gau_img20p)