# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 00:40:05 2022

@author: Kevin
"""
import cv2 
img = cv2.imread('opencv-logo-white.png', cv2.IMREAD_COLOR)
b, g, r = cv2.split(img)
b_img1 = img.copy()
b_img2 = img.copy()
b_img3 = img.copy()

# Question 4 Part a (only Blue)
b_img1[:,:,1] = 0 #green channel to 0 
b_img1[:,:,2] = 0 #red channel to 0
cv2.imshow('Blue Only', b_img1)
qu = cv2.waitKey(0)
if qu == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)
#---------------------------------------------------------

# Question 4 Part a (only Green)
b_img2[:,:,0] = 0 #blue channel to 0 
b_img2[:,:,2] = 0 #red channel to 0
cv2.imshow('Green Only', b_img2)
qi = cv2.waitKey(0)
if qi == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
#---------------------------------------------------------

# Question 4 Part a (only Red)
b_img3 = img.copy()
b_img3[:,:,0] = 0 #blue channel to 0 
b_img3[:,:,1] = 0 #red channel to 0
cv2.imshow('Red Only', b_img3)
qs = cv2.waitKey(0)
if qs == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)

#---------------------------------------------------------

# Question 4 Part b
b_merged = cv2.merge([b_img1[:,:,0], b_img2[:,:,1], b_img3[:,:,2]])
cv2.imshow('Merged Image', b_merged)
qt = cv2.waitKey(0)
if qt == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)

#---------------------------------------------------------

# Question 4 Part c
b_mg = cv2.merge([b_img1[:,:,0], b_img1[:,:,1], b_img3[:,:,2]])
cv2.imshow('Merged Image without Green', b_mg)
qp = cv2.waitKey(0)
if qp == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
#---------------------------------------------------------

# Question 4 Part d
b_mgr = cv2.merge([b_img3[:,:,2],b_img3[:,:,2],b_img3[:,:,2]])
cv2.imshow('Merged R', b_mgr)
qq = cv2.waitKey(0)
if qq == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)