# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test6.py
#@time:2018/05/13

import cv2
from pylab import  *
im= cv2.imread("2.jpg",0)
im = cv2.GaussianBlur(im, (3, 3), 0)
edges= cv2.Canny(im, 4, 12,apertureSize=3)
lines=cv2.HoughLinesP(edges,1,np.pi/180,120,minLineLength=30,maxLineGap=5)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(im,(x1,y1),(x2,y2),(0,120,215),1)


cv2.imshow("result",im)
cv2.imwrite("huofu2.jpg",im)
cv2.waitKey(0)
cv2.destroyAllWindows()
