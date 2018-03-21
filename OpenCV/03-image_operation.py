# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:33:08 2018

@author: pyadav
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


image1 = cv2.imread('img1.png')
image2 = cv2.imread('img2.jpg')


resized_image1 = cv2.resize(image1, (300, 300)) 
#snake
resized_image2 = cv2.resize(image2, (300, 300)) 

#size of image
#row,col,channel =  resized_image1.shape

#cv2.imwrite('img3.jpg',resized_image1 )

#image = cv2.addWeighted(resized_image1, 0.6,resized_image2, 0.4, 0)

img2gray = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(resized_image1, resized_image1, mask=mask_inv)
img2_fg = cv2.bitwise_and(resized_image2, resized_image2, mask=mask)

final_img = cv2.add(img1_bg, img2_fg)

cv2.imshow('Image1 BG', img1_bg)
cv2.imshow('Image2 FG', img2_fg)
cv2.imshow('Image2', resized_image2)
cv2.imshow('Image1', resized_image1)
cv2.imshow('gray', img2gray)
cv2.imshow('mask', mask)
cv2.imshow('mask INV', mask_inv)
cv2.imshow('Image1 BG', img1_bg)
cv2.imshow('Image2 FG', img2_fg)
cv2.imshow('Final Image', final_img)


imageArr = [resized_image1, resized_image2, mask, mask_inv, img1_bg, img2_fg, final_img]
imageTitle = ['image1', 'image2', 'mask', 'mask_inv', 'img1 BG', 'img2 FG', 'final img']

for imgNbr in range(7):
    subplotNbr = 240 + (imgNbr + 1)
    plt.subplot(subplotNbr)
    plt.title(imageTitle[imgNbr])
    plt.imshow(imageArr[imgNbr])
    plt.axis('off')
    

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.waitKey(1) #fix for mac