#!/usr/bin/env python3
# coding:utf-8
# @Author: yumu
# @Date:   2019-04-12
# @Email:   yumusb@foxmail.com
# @Last Modified by:   yumusb
# @Last Modified time: 2019-04-12
import tinify
import sys
filename = sys.argv[1]
tinify.key = "397NQLYZZm6LVVflHxFCN0wyYCWmpsjY"

source = tinify.from_file(filename)
source.to_file("fin_"+filename)