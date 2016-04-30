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
			'friends': 0,
			'visits': 0,
			'level': 0,
			'log': 0,
			'album': 0,
			'posts': 0,
			'board': 0,
			'public': 0,
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
		if status is None:
			info_dict['last'] = ' '
		else:
			info_dict['last'] = status[0]
		return info_dict

	def _get_num(self,pattern,html):
		for i in re.findall(pattern,html):
			for i in re.findall(r'\d+',i):
				if i == None:
					return 1234567889
				else:
					return int(i)

if __name__ == '__main__':
	HomePage()