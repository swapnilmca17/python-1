#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

__author__ = 'AJ Kipper'

# from bs4 import BeautifulSoup as bs
#
# with open('profile/206.html','r',encoding= 'utf-8') as webdata:
# 	soup = bs(webdata,'lxml')
# 	friends_num = soup.select('body > div.ssec > div > table > tr > td > span')[0].get_text()
# 	views_num = soup.select('body > div.ssec > div > span')[0].get_text()
# 	name = soup.select('body > div.ssec > p > b:nth-of-type(1)')[0].get_text()
# 	level = soup.select('body > div.ssec > p > b:nth-of-type(2)')[0].get_text()
# 	recent_time = soup.select('body > div.list > div:nth-of-type(2) > p.gs')[0].get_text()
# 	print(friends_num)
# 	print(views_num)
# 	print(name)
# 	print(level)
# 	print(recent_time)

from mdb import Engine

engine = Engine()

dict_data = {
	'Name' : '',
	'Friends' : 0,
	'Views' : 0,
}

result = []

data = engine.select('select * from profiles_info')
for j in range(len(data)):
	result.append({'Name' : data[j][1],'Gender' : data[j][2],'Visits' : data[j][3],'Level' : data[j][3],})


for i in result:
	print(i['Name'])
	print(i['Gender'])
	print(i['Visits'])