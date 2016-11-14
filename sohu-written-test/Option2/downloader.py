#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
downloader模块,完成对指定url下载网页信息
'''

__author__ = 'AJ Kipper'

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from logs import Logs

class Downloader(object):
	''''''
	def __init__(self,url):
		self.url = url
		#类实例初始化的时候进行网页请求
		self.req_info = self._get_request()
		#请求状态吗
		self.status_code = self.req_info.status_code
		#取时间精度到秒
		self.date_time = str(datetime.now())[:-7]
		self.soup = ''

	def _get_request(self):
		try:
			return requests.get(self.url,headers = self._set_headers())
		except:
			return False

	def _web_info(self):
		if self.status_code == 200 or self.req_info != False:
			self.soup = BeautifulSoup(self.req_info.text,'lxml')
			return True
		else:
			#如果状态码不等于200,写入错误日志
			logs = Logs(self.url,self.status_code,self.date_time)
			logs.logs_write()
			return False

	''''''
	def get_web_info(self):
		if self._web_info():
			#将网页信息打包成字典格式返回
			web_info = {
				'status_code' : self.status_code,
				'url' : self.url,
				'page_info' : self.soup
			}
			return web_info
		else:
			return False

	def _set_headers(self):
		#进行http头字段设置
		headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
			# 'Referer' : 'http://m.sohu.com/'
		}
		return headers

if __name__ == '__main__':
	Downloader()