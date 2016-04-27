#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import re
from bs4 import BeautifulSoup as bs


class friend_list_url(object):
	def __init__(self):
		self.next_url = []

	def get_next_url(self,page):
		soup = bs(page)
		for i in soup.find_all('div'):
			url = re.findall(r'http.*?curpage=.*?e=',str(i.a))
			#一个好友列表页面只有一个“下一页”链接，也就是url[0]
			try:
				self.next_url.append(url[0])
			except:
				pass
		return self.next_url
if __name__ == '__main__':
	fileobj = file('test.html','r+')
	html = fileobj.read()
	test = friend_list_url()
	print test.get_next_url(html)
