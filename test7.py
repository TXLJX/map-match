# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test7.py
#@time:2018/05/13

import  cv2
Img=cv2.imread("baidu.png")
RotateMatrix = cv2.getRotationMatrix2D(center=(Img.shape[1]/2, Img.shape[0]/2), angle=90, scale=1)
RotImg = cv2.warpAffine(Img, RotateMatrix, (Img.shape[0]*2, Img.shape[1]*2))
cv2.imshow("test",RotImg)
cv2.waitKey(0)