#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''这个模块解析主页信息'''

__author__ = 'AJ Kipper'

import re

class HomePage(object):

	def __init__(self):
		pass

	def get_info(self,html):
		status = []
		info_dict = {
			'name':'',
			'gender':'',
			'friends':'',
			'visits':'',
			'level':'',
			'log':'',
			'album':'',
			'posts':'',
			'board':'',
			'public':'',
			'last':''
			}
		info_dict['friends'] = self._get_num(r'他|她的好友.*?\(\d+\)',html)
		info_dict['visits'] = self._get_num(r'最近来访.*?\(\d+\)',html)
		info_dict['level'] = self._get_num(r'等级:.*?\d+',html)
		info_dict['log'] = self._get_num(r'日志.*?\(\d+\)',html)
		info_dict['album'] = self._get_num(r'相册.*?\(\d+\)',html)
		info_dict['posts'] = self._get_num(r'状态.*?\(\d+\)',html)
		info_dict['board'] = self._get_num(r'留言板.*?\(\d+\)',html)
		info_dict['public'] = self._get_num(r'公共主页.*?\(\d+\)',html)
		for i in re.findall(r'<title>.*?</title>',html):
			for i in re.findall(r'- .*?<',i):
				info_dict['name'] = i[2:len(i)-1]
		for i in re.findall(r'他|她的好友.*?\(\d+\)',html):
			if i[0:3] == '她':
				info_dict['gender'] = '女'
			else:
				info_dict['gender'] = '男'
		for i in re.findall(r'<p class="gs">.*?<\/p>',html):
			for i in re.findall(r'\d+.*\:\d+',i):
				status.append(i)
		try:
			if type(status[0]) != type(None):
				info_dict['last'] = str(status[0])
			else:
				info_dict['last'] = 'default'
		except:
			info_dict['last'] = 'default'
		return info_dict

	def _get_num(self,pattern,html):
		for i in re.findall(pattern,html):
			for i in re.findall(r'\d+',i):
					return i

if __name__ == '__main__':
	HomePage()