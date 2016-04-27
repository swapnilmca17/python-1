#-*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup as bs

fileobj = file('test.html','r+')
html = fileobj.read()

soup = bs(html)

for i in soup.body:
	try:
		if i.b != None:
			print i.b
	except:
		print 'None'

#print soup.body.div.table.tr.td.a


print len(list(soup.children))
# 1
print len(list(soup.descendants))

mat = r"[^?!>]<a.*?profil.*?<\/a>"

for i in soup.find_all('td'):
	link = str(i.a)
	for i in re.findall(r"<a href.*?;",link):
		for j in re.findall(r"http:.*?profil.*?p",link):
			print j
