#!/usr/bin/env python
#-*-coding: utf-8-*-


'register server module'

__author__ = 'AJ Kipper'
from random import randint
import emailserver

class register:
	def __init__(self,reg_email):
		#创建一个四个号码的伪随机数作为验证码
		code = randint(1000,2000)
		self.reg_email = reg_email
		self.code = str(code)
		self.send_status = False
	def verify(self):
		email = emailserver.email_server(self.reg_email,self.code)
		if email.send_email():
			print "Already sent!"
		else:
			print "Fail in send!"
		self.get_code()
	def get_code(self):
		code = raw_input('code:')
		while code != self.code:
			print 'Verification code is incorrect!'
			code = raw_input('code:')
		print "Verify success"

if __name__ == '__main__':
	#要发送邮箱地址
	test = register(['Email adress'])
	test.verify()
		
