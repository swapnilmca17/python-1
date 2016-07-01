#!/usr/bin/env python
#-*-coding: utf-8-*-
#Python 2.7.10


'register server module'

__author__ = 'AJ Kipper'
from random import randint
import emailserver
import sys

class register:
	def __init__(self,email):
		#产生一个4个数字的伪随机数作为验证码
		code = randint(1000,2000)
		self.reg_email = email
		self.code = str(code)
	def verify(self):
		email = emailserver.email_server(self.reg_email,self.code)
		if email.send_email():
			return(True,self.code)
		else:
			return(False,self.code)

if __name__ == '__main__':
	#获取发送邮箱地址
	test = register(sys.argv[1])
	#测试
	print(test.verify())
		
