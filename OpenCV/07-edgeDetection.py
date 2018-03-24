#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 11:49:05 2018

@author: pyadav
"""

import cv2

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0 , ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1 , ksize=5)
    edges = cv2.Canny(frame, 100, 200)
    
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)
    
    k = cv2.waitKey(5) & 0xFF
    # esc button
    if k == 27:
        print(k)
        break
 

cv2.destroyAllWindows()
camera.release()
cv2.waitKey(1) #fix for mac