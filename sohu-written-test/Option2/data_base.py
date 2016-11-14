#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5


'''
数据库操作接口
'''

__author__ = 'AJ Kipper'

import pymongo


class DataOper(object):

	def __init__(self):
		#进行数据库连接的初始化
		client = pymongo.MongoClient("localhost", 27017)
		self.db = client.sohu

		#插入一条url
	def insert(self,url):
		data = {
			'url' : url
		}
		self.db.one.insert(data)

		#删除一条url
	def delete(self,url):
		data = {
			'url' : url
		}
		self.db.one.delete_one(data)

		#查找所有urk
	def find(self):
		urls = []
		for i in self.db.one.find():
			urls.append(i['url'])
		return urls

		#判断一个url是否在数据库中,存在则返回True,不存在返回False
	def check(self,url):
		rec = False
		for i in  self.db.one.find({'url':url}):
			if i['url'] != None:
				rec = True
		return rec

if __name__ == '__main__':
	DataOper()

