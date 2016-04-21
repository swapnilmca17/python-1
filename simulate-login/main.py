#!/usr/bin/env Python
#-*- coding: utf-8 -*-
#--Python_Version:2.7.10

'''Main test for login'''

__author__ = 'AJ Kipper'

from renren_web_login import Login
import re
from urlparse import urljoin

userlogin = Login()
#填写登录账号和密码
username = "Your account"
password = "Your password"
userlogin.set_login_info(username,password)
loginurl = 'http://3g.renren.com'
html_doc = userlogin.login(loginurl)

#输出所有链接
links = re.findall('"((http|ftp)s?://.*?)"', html_doc)
for i in links:
	print i