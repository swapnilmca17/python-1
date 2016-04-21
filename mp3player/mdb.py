#!/usr/bin/python
# -*- coding: UTF-8 -*-

'MySQL Engine module'

__author__ = 'AJ Kipper'

import MySQLdb as mdb

class Engine(object):
	def __init__(self):
		pass

	def connect(self):
		con = mdb.connect("localhost","root","ha","Pydb")
		cur = con.cursor()
		self.con = con
		return cur

	def delete(self):
		id = raw_input("id: ")
		order = 'delete from Song where id = ' + str(id)
		cur = self.connect()
		cur.execute(order)
		self.con.commit()

	def insert(self):
		cur = self.connect()
		id = raw_input("id: ")
		name = raw_input("name: ")
		singer = raw_input("singer: ")
		path = raw_input("path: ")
		order = 'insert into Song values(' + id + '","' + name + '","' + singer + '","' + path + '")'
		print order
		cur.execute(order)
		self.con.commit()

	def select(self):
		cur = self.connect()
		cur.execute('select* from Song')
		values = cur.fetchall()
		return values


if __name__ == '__main__':
	Engine = Engine()
	Engine.connect()

