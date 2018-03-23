#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 16:52:07 2018

@author: Peeyush Yadav
"""

import cv2

img = cv2.imread('03-img.jpg')
grayScaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#problem with grayscale.. text is not readable 
retval, img_gray__threshold = cv2.threshold(grayScaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)

retval, img_threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

cv2.imshow('Image', img)
cv2.imshow('gaus', gaus)
cv2.imshow('Gray Image Threshold', img_gray__threshold)
cv2.imshow('Threshold Image', img_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac