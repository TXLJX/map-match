# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_cv特征提取.py
#@time:2018/05/13

import cv2
from pylab import *

im=cv2.imread("2.jpg")
#下采样
im_lower=cv2.pyrDown(im)
gray=cv2.cvtColor(im_lower,cv2.COLOR_RGB2GRAY)

#检测特征点
s=cv2.SURF()                #找不到
mask=uint8(ones(gray.shape))
keyponits=s.detect(gray,mask)
#显示结果及特征点
vis=cv2.cvtColor(gray,cv2.COLOR_RGB2GRAY)

for k in keyponits[::10]:
    cv2.circle(vis,(int(k.pt[0]),int(k.pt[1])),2,(0,255,0),2)
cv2.imshow("111",vis)
cv2.waitKey()