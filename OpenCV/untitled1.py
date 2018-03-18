#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:10:09 2017

@author: pyadav
"""

def x1 ():
    x=y=2
    return x,y

print(x1())
throw_frames=10

import cv2
import copy
import matplotlib.pyplot as plt
camera =cv2.VideoCapture(0)
for i in range(throw_frames):
        returnval, image = camera.read() #PIL format , if returnval = true then success

cv2.imshow("df",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

camera.release() 
