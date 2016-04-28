#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''获取好友列表中的下一页的链接'''

__author__ = 'AJ Kipper'

import re
from bs4 import BeautifulSoup as bs


class GetFriends(object):
	def __init__(self):
		pass

	def get_next_url(self,page):
		'''这个函数返回下一页链接'''
		soup = bs(page)
		#先找出所有的a标签
		for i in soup.find_all('a'):
			#正则表达式先匹配出下一页的a标签
			link = re.findall(r'<a href.*?>下一页<\/a>',str(i))
			try:
				#进一步把url匹配出来，并返回
				url = re.findall(r'http.*?curpage=.*?e=',link[0])
				return url[0]
			except:
				pass
if __name__ == '__main__':
	GetFriends()
