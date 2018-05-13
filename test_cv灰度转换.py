# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_cv灰度转换.py
#@time:2018/05/12

from PIL import  Image
import  cv2
from pylab import  *
im=cv2.imread("2.jpg")
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow("111",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
