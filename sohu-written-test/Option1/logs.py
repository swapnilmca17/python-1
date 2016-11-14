#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
错误日志写入模块
'''
__author__ = 'AJ Kipper'

class Logs(object):
	def __init__(self,url,status_code,date_time):
		self.test = ' '*3
		self.url = url
		#数据分别是时间.请求状态,请求链接
		self.logs = [str(date_time),str(status_code),str(self.url),'\n']

	def logs_write(self):
		try:
			#以添加模式打开文件,写入数据
			with open('error.log','a',encoding='utf-8') as file_obj:
				file_obj.writelines(self.test.join(self.logs))
		except Exception as e:
			print(e)



if __name__ == '__main__':
	Logs()