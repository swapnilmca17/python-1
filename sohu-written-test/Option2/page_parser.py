#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 3.5

'''
网页解析模块,得到指定url页面的全部链接
'''

__author__ = 'AJ Kipper'


from urllib.parse import urljoin
from urllib.parse import unquote
from datetime import datetime
from url_clean import Clean
from downloader import Downloader
from logs import Logs



class PageParser(object):
	''''''
	def __init__(self,root_url):
		self.root_url = root_url
		#类实例初始化的时候调用downloader模块进行url请求
		self.page = Downloader(root_url).get_web_info()['page_info']
		self.date_time = datetime.now()

		'''如果网页信息中存在404页面的信息,说明此url符合错误日志的url'''
	def _get_404(self):
		#通过bs中的select来获取
		info = self._get_select('header')
		try:
			for index in info:
				if index.text[:3] == '404':
					log = Logs(self.root_url,'404',str(self.date_time)[:-7])
					log.logs_write()
					return False
				else:
					return True
		except:
			return True

	''''''
	def _get_select(self,selector):
		if self.page != False:
			try:
				return self.page.select(selector)
			except:
				return False
		else:
			return False

	''''''
	def get_urls(self,urls = []):
		if self._get_404():
			all_links = self._get_select('a')
			if all_links != False:
				for link in all_links:
					link = str(link.get('href'))
					#页面中可能包括绝对url和相对url,要进行url的组合
					if 'http' in link[:4]:
						urls.append(unquote(link,encoding="utf-8"))
					else:
						urls.append(urljoin(self.root_url,unquote(link,encoding="utf-8")))
			#进行url的清洗
			urls = Clean(urls).main()
			return urls
		else:
			return []

if __name__ == '__main__':
	PageParser()