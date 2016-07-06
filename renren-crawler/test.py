#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

__author__ = 'AJ Kipper'

from bs4 import BeautifulSoup as bs
import pymongo

client = pymongo.MongoClient("localhost", 27017)

def data_insert(num):
	file_path = 'profile/' + str(num) + '.html'
	with open(file_path, 'r', encoding='utf-8') as webdata:
		soup = bs(webdata, 'lxml')
		try:
			friends_num = soup.select('body > div.ssec > div > table > tr > td > span')[0].get_text()
			views_num = soup.select('body > div.ssec > div > span')[0].get_text()
			name = soup.select('body > div.ssec > p > b:nth-of-type(1)')[0].get_text()
			level = soup.select('body > div.ssec > p > b:nth-of-type(2)')[0].get_text()
			recent_time = soup.select('body > div.list > div:nth-of-type(2) > p.gs')[0].get_text()
			data = {
				'friends': int(str(friends_num)[1:len(friends_num) - 1]),
				'views': int(str(views_num)[1:len(views_num) - 1]),
				'name': name,
				'level': level,
				'recent_time': str(recent_time)[0:10],
			}
			db = client.data_mining
			db.renren_data.insert(data)
		except:
			pass

for i in range(2,208):
	data_insert(i)

