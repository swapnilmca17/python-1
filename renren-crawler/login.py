#!/usr/bin/env python
#-*- coding:utf-8 -*-
#python 2.7.10

__author__ = 'AJ Kipper'

import sys
import urllib2
import urllib
import cookielib
 
#---------中文报错转码---------------
reload(sys)  
sys.setdefaultencoding("utf8")  
#----------------------------------

class Login(object):
     
    def __init__(self):
        self.username = ''
        self.password = ''
 
        self.cj = cookielib.LWPCookieJar()            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)    
     
    def set_login_info(self,username,password):
        '''设置用户登录信息'''
        self.email = username
        self.pwd = password
 
    def login(self,loginurl):
        '''登录网站'''
        
        loginparams = {'email':self.email, 'password':self.pwd}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)  
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
        return thePage        
         
if __name__ == '__main__':
    Login()
