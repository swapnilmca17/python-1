#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

'''数据库操作模块'''

__author__ = 'AJ Kipper'


import MySQLdb as mdb

class Engine(object):
	def __init__(self):
		pass

	def connect(self):
		#连接数据库，参数分别是数据库地址，用户名，密码，数据库名字
		con = mdb.connect("localhost","root","ha","crawler")
		cur = con.cursor()
		self.con = con
		return cur

	#也许用不到delete操作，但还是写了以免后期要用
	def delete(self):
		order = ''
		cur = self.connect()
		cur.execute(order)
		self.con.commit()

	def insert(self,info_list):
		cur = self.connect()
		#获取一个列表参数，将字段信息插入
		user_id = info_list[0]
		account_id = info_list[1]
		user_name = info_list[2]
		profile_url = info_list[3]
		order = "insert into friends_info values ('%d','%d','%s','%s');" % (user_id,account_id,user_name.encode('utf-8'),profile_url)
		cur.execute(order)
		self.con.commit()

	#将全部数据查询出来
	def select(self):
		cur = self.connect()
		order = 'select* from friends_info'
		cur.execute(order)
		values = cur.fetchall()
		return values


if __name__ == '__main__':
	Engine = Engine()
	Engine.connect()
