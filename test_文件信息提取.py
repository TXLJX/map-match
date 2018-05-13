# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:test_文件信息提取.py
#@time:2018/05/12
from PIL import  Image
from pylab import  *
def getImageInformation(filename):
    '''
    获取图片的行,列及选中点的坐标
    :param filename:
    :return:
    '''
    im=array(Image.open(filename))
    imSize=im.shape[:2]
    imshow(im)
    choicePoints=ginput(2)        #取前两次
    show()
    return imSize,choicePoints
imSize,choicePoint=getImageInformation("baidu2.png")
print(imSize)
print(choicePoint)