#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'


import MySQLdb as mdb

class Engine(object):
	def __init__(self):
		pass

	def connect(self):
		con = mdb.connect("localhost","root","ha","crawler")
		cur = con.cursor()
		self.con = con
		return cur

	def delete(self):
		order = ''
		cur = self.connect()
		cur.execute(order)
		self.con.commit()

	def insert(self):
		cur = self.connect()
		order = 'insert into friends_info values(' + id + '","' + account_id + '","' + user_name + '","' + profile_url + '","' + profile_path'")'
		cur.execute(order)
		self.con.commit()

	def select(self):
		cur = self.connect()
		order = 'select* from friends_info'
		cur.execute(order)
		values = cur.fetchall()
		return values


if __name__ == '__main__':
	Engine = Engine()
	Engine.connect()
