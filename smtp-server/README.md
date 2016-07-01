--------------
<h4 id = 'CV'>自述</h4>

--------------

######目录

1. [编程环境](#c1)
2. [项目说明](#c2)
3. [使用说明](#c3)

--------------

<h5 id = 'c1'>1. 编程环境</h5>

* 操作系统 : Mac OS X 10.10.5
* Python版本 : 2.7.10
* 涉及的Python标准库
  - smtplib
  - email
  - emailserver
  - random
  - sys.argv

<h5 id = 'c2'>2. 项目说明</h5>

一个自动发送邮箱验证码的小项目

---------------

1. 使用的邮箱协议是SMTP，使用smtplib库负责邮件发送，使用email.mine.text构造纯文本邮件

2. 验证码code使用的是random模块randint产生的4位伪随机整数

3. emailserver.py文件完成邮件构造和邮件发送功能，使用的邮箱服务器地址是smtp-mail.outlook.com

4. register.py文件完成产生伪随机数和验证功能

更具体的了解请访问Gitbook：[邮件发送脚本](https://ajkipper.gitbooks.io/python-projects/content/xiang_mu_ff1a_you_jian_fa_song.html)

---------------
<h5 id = 'c3'>3. 使用说明</h5>

* 在emailserver.py里面写上选择的邮件服务器

<pre><code>
#设置发送来源的邮箱地址
self.mail_account = 'Your email account'
self.mail_passwd = 'Your email password'
</code>
</pre>

* 在终端用Python命令运行register.py，并加上要发送的邮件即可

例子：

<pre><code>
 ~ python register.py 517450974@qq.com
(True, '1387')
 ~
</code>
</pre>
