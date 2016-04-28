#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import sys
import re
from bs4 import BeautifulSoup as bs
from mdb import Engine
#导入模拟登陆模块
from login import Login
#导入获取朋友列表页面模块
from get_friend_list import GetFriends
from get_friend_info import FriendInfo
#导入保存页面模块
from store_friends import StoreFriends


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
		self.login_url = 'http://3g.renren.com/friendlist.do?&sid=PwyGFaedzB81fFMISfrmve&kxlp77&htf=3'
		#设置一个计数，作为文件名字
		self.count = 1
		self.id_count = 1

	def get_page(self,url):
		return self.userlogin.login(url)

	def store_friends_page(self):
		'''这个函数将所有的好友列表页面保存下来'''
		#首先保存第一个页面
		page = self.get_page(self.login_url)
		store_friends = StoreFriends()
		store_friends.store(self.count,page)
		#因为显示总共有43页，所以设置range(44)就好
		for i in range(44):
			#输出一个提示
			print 'The %d page is saved successfully!' % self.count
			get_friends = GetFriends()
			#获取下一个页面的链接
			url = get_friends.get_next_url(page)
			if url != None:
				#将下一页链接作为抓取url
				page = self.get_page(url)
				store_friends = StoreFriends()
				self.count += 1
				#保存页面
				store_friends.store(self.count,page)
			else:
				continue

	def store_friends_info(self):
		for i in range(43):
			file_obj = file('friends/' + str(self.count) + '.html','r')
			page = file_obj.read()
			get_friend_info = FriendInfo(page)
			id_list = get_friend_info.get_id()
			name_list = get_friend_info.get_name()
			url_list = get_friend_info.get_url()
			engine = Engine()
			for i in range(5):
				print "%d : %d : %s : %s" % (self.id_count,int(id_list[i]),str(name_list[i]),str(url_list[i]))
				list_test = [self.id_count,int(id_list[i]),str(name_list[i]),str(url_list[i])]
				try:
					engine.insert(list_test)
				except:
					print 'Wrong'
				self.id_count += 1
			self.count += 1

if __name__ == '__main__':
	test = test()
	#test.store_friends_page()
	test.store_friends_info()
