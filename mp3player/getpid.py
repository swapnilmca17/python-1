#!/usr/bin/python
# -*- coding: UTF-8 -*-

'Get pid of iTunes'

__author__ = 'AJ Kipper'


import psutil
import re
import sys
 
 
def getpid():
	x = r'iTunes[^H]'
	p = psutil.get_process_list()
	for r in p:
		aa = str(r)
		if re.findall(x,aa):
			return aa.split('pid=')[1].split(',')[0]

if __name__ == '__main__':
	getpid = getpid()
	getpid()