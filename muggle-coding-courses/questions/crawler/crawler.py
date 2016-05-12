#!/usr/bin/env python
#!-*- coding : utf-8-*-

'''爬虫方面作业'''

__author__ = 'AJ Kipper'

import requests
from bs4 import BeautifulSoup
import time

'''
--------------------问题1----------------------
----------------第一周大作业---------------------
有些人爬取58浏览量view的时候出错了吧，因为58的反爬虫做了升级，所以要加上header信息
'''

def get_info(url):  #获取商品详细信息页的数据
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    cate = soup.select('#header > div.breadCrumb.f12 > span:nth-of-type(3) > a')[0].get_text()
    title = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1')[0].get_text()
    date = soup.select('#index_show > ul.mtit_con_left.fl > li.time')[0].get_text()
    price = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(1) > div.su_con > span')[0].get_text()
    quality = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_tit')[0].get_text()
    areas = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span')
    data = {
        'cate':cate,
        'title':title,
        'date':date,
        'price':price,
        'quality':quality,
        'area':list(areas[0].stripped_strings) if soup.find_all('span','c_25d') else None,
        'view':get_view(url)
    }
    print(data)

def get_view(url):  #获取浏览量
    infoid = url.split('?')[0].split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(infoid)

    '''这里要加上header信息'''

    headers = {'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
               'Cookie':r'id58=c5/ns1ct99sKkWWeFSQCAg==; city=bj; 58home=bj; ipcity=yiwu%7C%u4E49%u4E4C%7C0; als=0; myfeet_tooltip=end; bj58_id58s="NTZBZ1Mrd3JmSDdENzQ4NA=="; sessionid=021b1d13-b32e-407d-a76f-924ec040579e; bangbigtip2=1; 58tj_uuid=0ed4f4ba-f709-4c42-8972-77708fcfc553; new_session=0; new_uv=1; utm_source=; spm=; init_refer=; final_history={}; bj58_new_session=0; bj58_init_refer=""; bj58_new_uv=1'.format(str(infoid)),
               'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Host':'jst1.58.com',
               'Referer':r'http://bj.58.com/pingbandiannao/{}x.shtml'.format(str(infoid))
               }
    js = requests.get(api,headers = headers)
    #js = requests.get(api)
    view = js.text.split('=')[-1]
    return view

def get_links_info(page):  #page所需获取的信息的页数
    urls = ['http://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1,page)]
    links = []
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        link = soup.select('#infolist td.t a')
        time.sleep(5)
        for i in link:
            href = i.get('href')
            if href[:17] == 'http://bj.58.com/':
                get_info(href)

get_links_info(10)

'''爬取结果放在58info.txt文件里面'''