#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import sys
import re
from bs4 import BeautifulSoup as bs
from login import Login


#---------中文报错转码---------------
reload(sys)  
sys.setdefaultencoding("utf8")  
#----------------------------------

class test(object):
	def __init__(self):
		self.username = '517450974@qq.com'
		self.password = '19930518'
		self.userlogin = Login()
		self.userlogin.set_login_info(self.username,self.password)
		self.login_url = 'http://3g.renren.com/profile.do?id=425186021&sid=PwyGFaedzB81fFMISfrmve&160evn'
		self.friendlist_url = [self.login_url]
	def get_page(self,url):
		return userlogin.login(url)