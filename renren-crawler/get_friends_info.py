#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import re
from bs4 import BeautifulSoup as bs



class test(object):

	def __init__(self,page):
		self.id_list = []
		self.name_list = []
		self.url_list = []
		self.soup = bs(page)

	def get_id(self):
		for i in self.soup.find_all('td'):
			for i in re.findall(r"id=\d{8,12}",str(i.a)):
				for friend_id in re.findall(r"\d{8,12}",i):
					if friend_id not in self.id_list:
						self.id_list.append(friend_id)
					else:
						pass
		return self.id_list
	def get_name(self):
		for i in self.soup.find_all('td'):
			for i in re.findall(r'alt=".*?"',str(i.a)):
				for name in re.findall(r'"[^renren].*?"',i):
					if name not in self.name_list:
						self.name_list.append(name)
					else:
						pass
		return self.name_list
	def get_url(self):
		for i in range(len(self.id_list)):
			url = 'http://3g.renren.com/profile.do?id=' + self.id_list[i] + '&sid=PwyGFaedzB81fFMISfrmve&gevqvo'
			if url not in self.url_list:
				self.url_list.append(url)
			else:
				pass
		return self.url_list

if __name__ == '__main__':
	fileobj = file('test.html','r+')
	html = fileobj.read()
	test = test(html)
	for i in range(5):
		try:
			print test.get_id()[i] + ":" + test.get_name()[i] + ":" + test.get_url()[i]
		except:
			pass
