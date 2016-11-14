#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
url清洗模块
'''

__author__ = 'AJ Kipper'

class Clean(object):
	''''''
	def __init__(self,urls):
		self.urls = urls
		self.url_test = []

	def _test(self):
		#对不是m.sohu.com域名的页面去除
		for i in self.urls:
			if 'http://m.sohu.com/' not in str(i)[:26]  or i in self.url_test:
				pass
			else:
				self.url_test.append(i)

	def main(self):
		self._test()
		return self.url_test

if __name__ == '__main__':
	Clean()