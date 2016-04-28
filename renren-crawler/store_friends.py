#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''这个模块用来保存朋友列表页面'''

__author__ = 'AJ Kipper'

import os

class StoreFriends(object):

	def __init__(self):
		#判断是否已经存在friends目录
		if os.path.exists('friends'):
			pass
		else:
			#如不存在则新建一个
			os.popen('mkdir friends')

	def store(self,count,page):
		#构建路径
		friends_path = 'friends/' + str(count) + '.html'
		file_obj = open(friends_path,"w+")
		file_obj.write(page)
		file_obj.close()

if __name__ == '__main__':
	StoreFriends()