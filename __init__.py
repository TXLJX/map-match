# -*- coding:utf-8 -*-
# @author:lijinxi
# @file:__init__.py.py
# @time:2018/05/12
from PIL import Image
from pylab import *
import math
import cv2
import random


def getImageInformation(filename):
    '''
    获取初始图片的行,列像素值及选取的匹配两点
    :param filename:
    :return:
    '''
    im = array(Image.open(filename))
    if im is None:
        raise IOError("图片文件有误................")
    imSize = im.shape[:2]  # 行,列
    imshow(im)
    choicePoints = ginput(3)
    show()
    return list(imSize), choicePoints


def convert_distance_angle(Point1, Point2):
    '''
    勾股定理及反正切
    :param Point1:
    :param Point2:
    :return:
    '''
    x1, y1 = Point1
    x2, y2 = Point2
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    angle = -math.atan((y2 - y1) / (x2 - x1))
    print("distance,angle", distance, angle)
    return distance, angle


def match_two_points(distance1, angle1, distance2, angle2):
    '''
    设置缩放比
    :param distance1:
    :param angle1:
    :param distance2:
    :param angle2:
    :return:
    '''
    times = distance2 / distance1
    minusangle = angle2 - angle1
    print("times,angle", times, minusangle)
    return times, minusangle


def convert_points(Point1, Point2, changePoint, angle):
    '''
    将两点基点重合,变换图片四个顶点
    :param Point1: 小图片基点1
    :param Point2: 大图片基点2
    :param changePoint: 相对于基点1的坐标(同一个坐标系)
    :param angle: 逆时针旋转角度
    :return:
    '''
    x1, y1 = Point1
    x2, y2 = Point2
    cx, cy = changePoint
    rx, ry = ((cx - x1) * cos(-angle) - (cy - y1) * sin(-angle) + x2), (
            (cx - x1) * sin(-angle) + (cy - y1) * cos(-angle) + y2)
    return (rx, ry)


def get_roi_fourpoints(imSize1, Point1, Point2, angle=0):
    '''
    寻找映射的ROI
    :param imSize1: 小图片(行,列)
    :param Point1: 小图片上选定的第一个点,以此做基点重合
    :param Point2:大图片上基点
    :return:
    '''
    # 区域较小的图的四个顶点,精度一致的前提下
    fourPoints = [(0, 0), (imSize1[1], 0), (imSize1[1], imSize1[0]), (0, imSize1[0])]
    # 变换到第二个坐标系中
    newFourPoints = [convert_points(Point1, Point2, changePoint, angle) for changePoint in fourPoints]
    print(newFourPoints)
    return newFourPoints


def adaptFormat(filename1, filename2, imSize1, imSize2, angle1, basePoint):
    '''
    处理图片兼容性问题,主要是在手机和电脑上截图使用的格式不完全一致
    :param filename1: 小图片文件
    :param filename2: 大图片文件
    :param imSize1: 图片1的行和列
    :param imSize2: 图片的行和列
    :param angle:旋转角度
    :return:
    '''
    im1 = cv2.imread(filename1)
    cv2.resize(im1, (imSize1[1], imSize1[0]), im1)
    print(angle1)
    #定点旋转
    RotateMatrix = cv2.getRotationMatrix2D(center=(basePoint[0], basePoint[1]), angle=(180 * angle1 / np.pi), scale=1)
    RotImg = cv2.warpAffine(im1, RotateMatrix, (im1.shape[0]*2 , im1.shape[1] *2))
    imsave("temp1.png", RotImg)
    im1 = array(cv2.imread("temp1.png"))
    im2 = Image.open(filename2)
    im2 = im2.resize((imSize2[1], imSize2[0]))
    imsave("temp2.png", im2)
    im2 = array(cv2.imread("temp2.png"))
    return im1, im2


def addROI(Point1, Point3, im1, im2):
    '''
    定位ROI,多边形ROI不易寻找,选择矩形,对图片进行相应旋转即可
    :param Point1: 较小的图片第一个顶点(x,y)
    :param Point3: 较小第三个第三个顶点
    :param im1:
    :param im2:较大的图片
    :return:
    '''
    i = random.randint(1, 100)
    imageROI = im2[int(Point1[1]):int(Point3[1]), int(Point1[0]):int(Point3[0])]
    imageROI2 = im1[0:int(Point3[1]) - int(Point1[1]), 0:int(Point3[0]) - int(Point1[0])]
    cv2.addWeighted(imageROI, 0.5, imageROI2, 0.5, 0, imageROI)
    im2[int(Point1[1]):int(Point3[1]), int(Point1[0]):int(Point3[0])] = imageROI
    imshow(im2)
    show()
    imsave("test" + str(i) + ".png", im2)
    print("图片test" + str(i) + ".png成功创建.....................")


def method(filename1, filename2):
    '''
     要求一图片是另一图片所含的子集,处理图片精度及旋转问题
    :param filename1:
    :param filename2:
    :return:
    '''
    # 读取图片获取信息
    imSize1, choicePoints_1 = getImageInformation(filename1)
    imSize2, choicePoints_2 = getImageInformation(filename2)
    # 求尺度
    distances1, angle1 = convert_distance_angle(choicePoints_1[0], choicePoints_1[1])
    distances2, angle2 = convert_distance_angle(choicePoints_2[0], choicePoints_2[1])
    times, minusangle = match_two_points(distances1, angle1, distances2, angle2)
    Point1 = list(choicePoints_1[0])
    Point2 = list(choicePoints_2[0])
    if (times > 1):
        imSize1[0], imSize1[1] = int(imSize1[0] * times), int(imSize1[1] * times)  # 将图片一变变换到相同尺度
        Point1[0], Point1[1] = Point1[0] * times, Point1[1] * times  # 第一个基点进行相应变换
    else:
        imSize2[0], imSize2[1] = int(imSize2[0] / times), int(imSize2[1] / times)  # 图片二变换到相同尺度值
        Point2[0], Point2[1] = Point2[0] / times, Point2[1] / times
    # 相同精度下判断哪个图大
    print(imSize1, imSize2)
    if (imSize1[0] < imSize2[0] and imSize1[1] < imSize2[1]):
        newFourPoints = get_roi_fourpoints(imSize1, Point1, Point2)
        Point_1, Point_2, Point_3, Point_4 = newFourPoints
        # 重新输入图片,由于多边形ROI不易提取故先进行旋转和缩放
        im1, im2 = adaptFormat(filename1, filename2, imSize1, imSize2, minusangle, Point1)
        ''''
        im1 = Image.open(filename1)
        im1 = im1.resize((imSize1[1], imSize1[0]))
        im1.rotate(minusangle)
        im1 = array(im1)  # 下一步切片
        im2 = Image.open(filename2)
        im2 = im2.resize((imSize2[1], imSize2[0]))
        im2 = array(im2)
        '''
        addROI(Point_1, Point_3, im1, im2)
    elif (imSize1[0] > imSize2[0] and imSize1[1] > imSize2[1]):
        newFourPoints = get_roi_fourpoints(imSize2, Point2, Point1)
        Point_1, Point_2, Point_3, Point_4 = newFourPoints
        # 处理图片2
        im1, im2 = adaptFormat(filename2, filename1, imSize2, imSize1, -minusangle, Point2)
        ''''     ###未封装的代码###
        im2 = Image.open(filename2)
        im2 = im2.resize((imSize2[1], imSize2[0]))
        im2.rotate(-minusangle)
        im2 = array(im2)
        print(im2.shape[:2])
        im1 = Image.open(filename1)
        im1 = im1.resize((imSize1[1], imSize1[0]))  # width,height
        im1 = array(im1)
        print(im1.shape[:2])
        '''
        addROI(Point_1, Point_3, im2, im1)
    else:
        raise AssertionError("输入的图片不符合要求...........")


if __name__ == '__main__':
    # method("baidu.png", "gaode.png")
    # method("baidu.png","tencent.png")
    # method("gaode.png","tencent.png")
    # method("baidu.png", "microsoft.png")
    method("gaode.png", "2.jpg")
