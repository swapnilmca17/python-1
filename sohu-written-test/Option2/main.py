#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
主控模块
'''

__author__ = 'AJ Kipper'


from page_parser import PageParser
from multiprocessing import Pool
from data_base import DataOper


#数据库操作模块实例化
data = DataOper()
#设置根url
root_url = 'http://m.sohu.com/'

def get_urls(url):
	global urls,counter
	try:
		#可选,进行抓取的url写入一个文件中,但会增加I/O操作
		# with open('url_list.txt','a') as test:
		# 	test.write(url + '\n')
		data.delete(url)
		print(url)
		analysis = PageParser(url)
		for i in analysis.get_urls():
			if data.check(i):
				data.delete(i)
			else:
				data.insert(i)
	except:
		pass

#先将根url放在数据库中
data.insert(root_url)

#设置多进程进行抓取
pool = Pool(processes=10)
pool.map(get_urls,data.find())
pool.close()
pool.join()
