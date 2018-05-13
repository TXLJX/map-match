# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_python基本图像处理.py
#@time:2018/05/12

from PIL import  Image
im1=Image.open("baidu2.png")
im1=im1.rotate(45)
im1.save("2.jpg")