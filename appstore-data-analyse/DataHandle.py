#!/usr/bin/env Python
#-*- coding: utf-8 -*-
#--Python_Version:2.7.9

'.json to .csv module'
__version__ = 0.1

__author__ = "AJ Kipper"

from pandas import DataFrame
import json
import sys


json_file = file('//Users/Jason/Desktop/appstore.json','r')

def json_to_dict(json_file):
	'''将json格式数据存储到字典格式中'''
	#创建一个空的字典，用来存储json数据
	dict_data = {}
	index = 1
	for line in json_file:
		line_data = json.loads(line)
		#以1开始为索引逐行增加到字典中
		dict_data[str(index)] = line_data
		index += 1
	return dict_data

#将返回的dict_data转换成DataFrame格式，目的是更方便写入.csv文件中
frame = DataFrame(json_to_dict(json_file))
#先用frame.T转置矩阵（更易浏览），再用DataFrame数据对象的.to_csv方法写入.csv文件中,na_rep将空的值设置为NULL
frame.T.to_csv('//Users/Jason/KDD/API/appstore.csv',na_rep = 'NULL')