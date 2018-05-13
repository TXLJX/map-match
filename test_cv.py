# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_cv.py
#@time:2018/05/12

import cv2
from PIL import  Image
from pylab import  *

im1=array(Image.open("baidu2.png"))
im2=array(Image.open("gaode.png"))
imROI=im1[200:600,400:800]
#im2ROI=im1[400:800,200:600]
im2ROI=im2[100:500,100:500]
cv2.addWeighted(imROI,0.5,im2ROI,0.5,0,imROI)
im1[200:600,400:800]=imROI
imshow(im1)
show()