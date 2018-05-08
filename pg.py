# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:46:28 2018

@author: Administrator
"""
import cv2
import os
import numpy as np
import time

def img2txt(img):
    serarr=['@','#','$','%','&','?','*','o','/','{','[','(','|','!','^','~','-','_',':',';',',','.','`',' ']
    count=len(serarr)

    asd =''#储存字符串
    for h in range(img.shape[0]):#h
       for w in range(img.shape[1]):#w
          gray =img[h,w]
          asd=asd+serarr[int(gray/(255/(count-1)))]   #灰度越大 越接近白 使用越小的字符例如空字符' '
       asd=asd+'\r\n'
       
    print(asd)
    return asd
#    imwrite() 
#####################################
#打开图片
img = cv2.imread('pg2.jpg',0)
img=cv2.resize(img,(125,60))


asd=img2txt(img)#调用函数

#保存数据到txt
f = open("text.txt",'w')
f.write(asd)
f.close()






