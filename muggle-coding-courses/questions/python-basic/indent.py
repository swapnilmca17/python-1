#!/usr/bin/env python
#-*- coding : utf-8-*-
#python 3.5

'''Some errors in code indent'''

__author__ = 'AJ Kipper'

'''
--------------------问题1----------------------
----------------1_2code_of_video--------------
'''

from bs4 import BeautifulSoup
  
info = []
with open('new_index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, "lxml")
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
  
for image,title,desc,rate,cate in zip(images,titles,descs,rates,cates):
    data = {
        'image': image.get('src'),
        'title': title.get_text(),
        'desc' : desc.get_text(),
        'rate' : rate.get_text(),
        'cate' : list(cate.stripped_strings)
            }
    #注意这里要进行缩进，在for循环里面
    info.append(data)
'''
错误示范
如果没有缩进的话，得到的永远是最后一项data数据
info.append(data)
'''
for i in info:
    if float(i['rate'])>3:
        print(i['title'],i['cate'])
'''
------------输出结果------------
Sardinia's top 10 beaches ['fun', 'Wow']
How to get tanned ['butt', 'NSFW']
How to be an Aussie beach bum ['sea']

'''