#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import os

class test(object):

	def __init__(self):
		if os.path.exists('profile'):
			pass
		else:
			os.popen('mkdir profile')

	def store(self,user_id,page):
		profile_path = 'profile/' + str(user_id) + '.html'
		file_obj = open(profile_path,"w+")
		file_obj.write(page)
		file_obj.close()

if __name__ == '__main__':
	file_obj = file('test.html','r+')
	page = file_obj.read()
	print page
	test = test()
	test.store(1,page)