#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:52:07 2018

@author: Peeyush Yadav
"""

import cv2
import numpy as np

img = cv2.imread('05-img.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red_low = np.array([0,110,110])
red_high = np.array([255,255,255])

mask = cv2.inRange(hsv, red_low, red_high)
final_img = cv2.bitwise_and(img, img, mask=mask)

kernel = np.ones((5,5), np.uint8)

#This kernel is overlapped over the picture to compute maximum pixel value.
#the size of an object in white shade or bright shade increases while the size of an object in black shade or dark shade decreases.
dilation = cv2.dilate(mask, kernel, iterations=1)

#the pixel value computed here is minimum rather than maximum in dilation.
#the size of an object in dark shade or black shade increases, while it decreases in white shade or bright shade.
erosion = cv2.erode(mask, kernel, iterations=1)


opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) 
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) 

cv2.imshow('Image', img)
cv2.imshow('mask', mask)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac