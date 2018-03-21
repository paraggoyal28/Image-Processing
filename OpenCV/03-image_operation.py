# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:33:08 2018

@author: pyadav
"""

import cv2
import numpy as np


image = cv2.imread('demo.jpg')

cv2.line(image, (10,10), (100,200), (0,255,255), 9)

pts = np.array([[60,60],[90,100], [120,150], [90,30]], np.int32)
cv2.polylines(image, [pts], True, (255,0,255), 7)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Bitcoin', (100,100), font, 1, (255,255,255))


cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1) #fix for mac