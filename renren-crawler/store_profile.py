#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''保存好友主页页面'''

__author__ = 'AJ Kipper'

import os

class ProfileInfo(object):

	def __init__(self):
		#判断是否存在profile文件夹
		if os.path.exists('profile'):
			pass
		else:
			#如果没有则创建一个
			os.popen('mkdir profile')

	def store(self,user_id,page):
		#以user_id为名保存在tml文件
		profile_path = 'profile/' + str(user_id) + '.html'
		file_obj = open(profile_path,"w+")
		file_obj.write(page)
		file_obj.close()

if __name__ == '__main__':
	ProfileInfo()