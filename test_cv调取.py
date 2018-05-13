# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_cv调取.py
#@time:2018/05/12
import  cv2
from PIL import  Image
from pylab import  *
im1=Image.open("baidu.png")
im2=im1.rotate(15)
im3=array(Image.open("2.jpg"))
im2=array(im2)
cv2.addWeighted(im2,0.5,im3,0.5,0.3,im2)
cv2.imshow("",im2)
cv2.waitKey(0)
