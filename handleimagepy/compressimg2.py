#!/usr/bin/env python3
# coding:utf-8
# @Author: yumu
# @Date:   2019-04-12
# @Email:   yumusb@foxmail.com
# @Last Modified by:   yumusb
# @Last Modified time: 2019-07-18
import tinify
import sys
import os
def compress(filename):
	tinify.key = "397NQLYZZm6LVVflHxFCN0wyYCWmpsjY"
	print(filename)
	source = tinify.from_file(filename)
	tmp = filename+".bak"
	source.to_file(tmp)
	if(os.path.getsize(filename)>os.path.getsize(tmp)):
		print(f"节约空间{(os.path.getsize(filename)-os.path.getsize(tmp))/1024}KB")
		os.remove(filename)
		os.rename(tmp,filename)
	else:
		print("已经压缩过了")
		os.remove(tmp)
path=sys.argv[1]
for root, dirs, files in os.walk(path):
    for name in files:
        filename = os.path.join(root, name)
        if filename.split(".")[1] in ["png","jpeg","jpg"]: 
        	compress(filename)