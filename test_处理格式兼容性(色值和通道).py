# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_处理格式兼容性(色值和通道).py
#@time:2018/05/13

from PIL import  Image
from pylab import  *
import  cv2
im1=Image.open("baidu.png")
im1=im1.resize((800,800))
''''
imshow(im1)
show()
imsave("zzz1.png",im1)
'''
im1=cv2.imread("microsoft.png")
im2=cv2.imread("zzz1.png")
im1=array(im1)
imROI=im1[100:400,100:400]
im2=array(im2)
imROI2=im2[100:400,100:400]
cv2.addWeighted(imROI,0.5,imROI2,0.5,0,imROI)
imshow(imROI)
show()
#cv2.imshow("11",imROI)
#cv2.waitKey(0)
