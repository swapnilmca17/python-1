#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
主控模块
'''

__author__ = 'AJ Kipper'

import threading
from page_parser import PageParser
from bloom_filter import BloomFilter

root_url = 'http://m.sodu.com'

class Test:

	#这三个都是多线程共享的变量
	f = BloomFilter(0.0001, 10000000)
	urls = ['http://m.sodu.com',]
	count = 0

	@classmethod
	def get_url(cls):
		url = Test.urls.pop(0)
		while Test.f.is_element_exist(url) == True:
			url = Test.urls.pop(0)
		Test.f.insert_element(url)
		# 可选,进行抓取的url写入一个文件中,但会增加I/O操作
		# with open('urls.txt', 'a') as file_obj:
		# 	file_obj.write(url + '\n')
		return url

	@classmethod
	def get_urls(cls):
		while len(Test.urls) > 0:
			url = Test.get_url()
			try:
				Test.count += 1
				print(Test.count,url)
				analysis = PageParser(url)
				test = analysis.get_urls()
				Test.urls += test
			except:
				pass

if __name__ == '__main__':
	#设置多线程榨取
	for i in range(100):
		thread_pool = []
		th = threading.Thread(target=Test.get_urls)
		thread_pool.append(th)
		thread_pool[i].start()
		for thread in thread_pool:
			threading.Thread.join(thread)