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

	def delete(self,statement):
		cur = self.connect()
		cur.execute(statement)
		self.con.commit()

	def insert(self,statement):
		cur = self.connect()
		cur.execute(statement)
		self.con.commit()

	def select(self,statement):
		cur = self.connect()
		cur.execute(statement)
		values = cur.fetchall()
		return values


if __name__ == '__main__':
	Engine = Engine()
	Engine.connect()
