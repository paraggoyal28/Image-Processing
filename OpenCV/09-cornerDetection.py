#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:04:01 2018

@author: Peeyush Yadav
"""

import cv2
import numpy as np

img = cv2.imread('09-img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


corners = cv2.goodFeaturesToTrack(gray, 100, .01, 10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0,255,0))


cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac
