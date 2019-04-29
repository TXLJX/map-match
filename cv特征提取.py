# -*- coding:utf-8 -*-
#@author:lijinxi
#@file:cv特征提取.py
#@time:2018/05/13

import cv2
import numpy


def main():
    img = cv2.imread("lena.png")
    cv2.imshow('Input Image', img)
    cv2.waitKey(0)
    # 检测
    akaze = cv2.xfeatures2d.SIFT_create()
    keypoints = akaze.detect(img, None)
    img2 = img.copy()
    img2 = cv2.drawKeypoints(img, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected SIFT keypoints', img2)
    cv2.imwrite('sift.jpg',img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()