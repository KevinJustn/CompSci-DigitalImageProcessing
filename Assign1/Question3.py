# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:52:40 2022

@author: Kevin
"""
#No Camera, using cv2.imread()
# Question 3 Part a
import cv2
img = cv2.imread('backyard.png')
cv2.imshow('Colored Image',img)
q = cv2.waitKey(0)
if q == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    cv2.waitKey(1)

# ---------------------------------------------------------

#Question 3 Part b
import skimage.io as io
import pylab
from matplotlib import pyplot as plt
hist = io.imread('backyard.png')
io.imshow(hist)
f = pylab.figure()
f.show(plt.hist(hist.flatten(), bins=256))

# ---------------------------------------------------------

#Question 3 Part c
import cv2 as cv3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to input image.', default='backyard.png')
args = parser.parse_args()
src = cv3.imread(cv3.samples.findFile(args.input))
src = cv3.cvtColor(src, cv3.COLOR_BGR2GRAY)
dst = cv3.equalizeHist(src)
io.imshow(dst)
g = pylab.figure()
g.show(plt.hist(dst.flatten(), bins=256))

#cv3.imshow('Equalized Image', dst)
#qr = cv3.waitKey(0)
#if qr == 27:         # wait for ESC key to exit
#    cv3.destroyAllWindows()
#    cv3.waitKey(1)
