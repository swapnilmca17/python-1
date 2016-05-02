#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

__author__ = 'AJ Kipper'

from bs4 import BeautifulSoup as bs

with open('profile/1.html','r') as webdata:
	soup = bs(webdata,'lxml')
	titles = soup.select('body > div.sec.nav > a')
	posts = soup.select('body > div.list > div')
	tag = soup.select('body > div:nth-child(5) > table > tbody > tr:nth-child(3) > td:nth-child(2) > a')


for i in posts:
	print (i)

print (tag)



'''
body > div.sec.nav > a:nth-child(1)
body > div.list > div:nth-child(2)
body > div:nth-child(5) > table > tbody > tr:nth-child(3) > td:nth-child(2) > a
'''