#!/usr/bin/env python3
# coding:utf-8
# @Author: yumu
# @Date:   2019-04-12
# @Email:   yumusb@foxmail.com
# @Last Modified by:   yumusb
# @Last Modified time: 2019-04-12

from PIL import Image 
import os
def pic_webp(picpath): 
	imagePath = picpath.split(".")[0] #文件名称 
	outputPath = imagePath + ".webp" #输出文件名称 
	im = Image.open(picpath) #读入文件 
	im.save(outputPath,"WEBP") #保存 
for (filename) in os.listdir("./"): 
	if filename.split(".")[1] in ["png","jpeg","jpg"]: 
		pic_webp(filename)