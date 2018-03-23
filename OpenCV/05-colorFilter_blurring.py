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

kernel = np.ones((9,9), np.float32)/81

smoothed = cv2.filter2D(final_img, -1, kernel)

blur = cv2.GaussianBlur(final_img, (9,9), 0)

medianBlur = cv2.medianBlur(final_img, 15)

cv2.imshow('Image', img)
cv2.imshow('mask', mask)
cv2.imshow('Image HSV', hsv)
cv2.imshow('Final Img', final_img)
cv2.imshow('smoothed', smoothed)
cv2.imshow('blur', blur)
cv2.imshow('median blur', medianBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac