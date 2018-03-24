#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:04:01 2018

@author: Peeyush Yadav
"""

import cv2
import numpy as np

img = cv2.imread('08-image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

#reading as gray image
template = cv2.imread('08-searchImg.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED) 
loc = np.where( res >= .69)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+ w, pt[1]+h), (0,0,255), 2)

cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac
