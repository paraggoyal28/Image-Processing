#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 21:16:14 2018

@author: pyadav
"""

import cv2

videoObject = cv2.VideoCapture(0)

#videoObject.set(cv2.CAP_PROP_FRAME_WIDTH, 360)
#videoObject.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20, (360,480))

while True :
    ret, frame = videoObject.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', frame)
    cv2.imshow('Video1', gray)
  
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
videoObject.release()
out.release()
cv2.destroyAllWindows()