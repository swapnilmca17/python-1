<h4 id = 'CV'>自述</h4>

自己平时用Python写的小项目，各方面都有。

部分项目的编写和设计过程放在Gitbook上面，有兴趣可以访问[Python项目笔记](https://www.gitbook.com/book/ajkipper/python-projects/details)

-------------

**目录**

1. [邮件发送脚本 -- smtp-server](#c1)
2. [Mp3播放控制 -- mp3player](#c2)
3. [AppStore数据分析 -- appstore-data-analyse](#c3)
4. [人人网爬虫 -- renren-crawler](#c4)
5. [麻瓜编程课程 -- muggle-coding-course](#c5)
6. [Django搭建个人博客 -- Build a personal blog by Django](#c6)

-------------------

<h5 id = 'c1'>1. 邮件发送脚本 -- smtp-server</h5>

**项目说明**

一个自动发送邮箱验证码的程序

--------------------

1. 使用的邮箱协议是SMTP，使用smtplib库负责邮件发送，使用email.mine.text构造纯文本邮件

2. 验证码code使用的是random模块randint产生的4位伪随机整数

3. emailserver.py文件完成邮件构造和邮件发送功能，使用的邮箱服务器地址是smtp-mail.outlook.com

4. register.py文件完成产生伪随机数和验证功能

直接访问[https://github.com/AJKipper/PythonProject/tree/master/smtp-server](https://github.com/AJKipper/PythonProject/tree/master/smtp-server)

具体的项目讲解已经放在我的Gitbook上，欢迎访问：[项目：邮件发送脚本](https://ajkipper.gitbooks.io/python-projects/content/xiang_mu_ff1a_you_jian_fa_song.html)

-------------------

<h5 id = 'c2'>2. Mp3播放控制 -- mp3player</h5>

**项目说明**

一个Mp3播放器(仅逻辑实现)

---------------

1. 歌曲本身存在硬盘，路径存储在MySQL数据库

2. 终端界面实现控制歌曲的播放，暂定，继续操作

3. 终端界面实现歌曲在数据库的存储，删除操作

直接访问[https://github.com/AJKipper/PythonProject/tree/master/mp3player](https://github.com/AJKipper/PythonProject/tree/master/mp3player)

-------------------

<h5 id = 'c3'>3. AppStore数据分析 -- appstore-data-analyse</h5>

这是一个利用Python分析一个json数据，并可视化输出结果的小项目
数据的来源是一个叫数据堂的网站：[http://www.datatang.com/data/46084](http://www.datatang.com/data/46084)

具体的项目讲解已经放在我的Gitbook上，欢迎访问：[项目：AppStore数据分析](https://ajkipper.gitbooks.io/python-projects/content/xiang_mu_ff1a_appstore_shu_ju_fen_xi.html)

直接访问[https://github.com/AJKipper/PythonProject/tree/master/appstore-data-analyse](https://github.com/AJKipper/PythonProject/tree/master/appstore-data-analyse)

-------------------

<h5 id = 'c4'>4. 人人网爬虫 -- renren-crawler</h5>

人人网爬虫项目。

---

抓取内容	

* 我的好友列表所有页面(一个页面只展示5个好友信息)
* 好友的基本信息(人人网id，名字，主页链接)
* 所有好友主页的页面

直接访问[https://github.com/AJKipper/PythonProject/tree/master/renren-crawler](https://github.com/AJKipper/PythonProject/tree/master/renren-crawler)

具体的项目讲解已经放在我的Gitbook上，欢迎访问：[项目：人人网爬虫](https://ajkipper.gitbooks.io/python-projects/content/ren_ren_wang_pa_chong.html)

----------


<h5 id = 'c5'>5. 麻瓜编程课程 -- muggle-coding-course</h5>

**项目说明**

麻瓜编程是一个在网易云课堂做Python，爬虫，Django等相关编程技术课程的创业团队，而我之前在这个团队里面实习，所以把自己做的一些项目也放在了这里，里面的项目涉及爬虫，Django，MongoDB，Jupyter等，有兴趣可以直接访问[https://github.com/AJKipper/PythonProjects/tree/master/muggle-coding-courses](https://github.com/AJKipper/PythonProjects/tree/master/muggle-coding-courses)


----
<h5 id = 'c6'>6. Django搭建个人博客 -- Build a personal blog by Django</h5>

**项目说明**

1. 项目使用Django框架，数据库使用Sqlite，前端由自己编写，略微简洁；文章排版使用了Markdown_deux插件。
2. 已经部署在阿里云ESC服务器上面，部署方式为Django+uwsgi+nginx。
3. 这个项目出于兴趣而做，时间为一个星期。过程中掌握了使用Django快速开发博客的流程，以及Django框架在服务器部署的基本技术。
4. 网站站点展示可以访问[http://120.27.46.91:8000/](http://120.27.46.91:8000/)(暂时没有做域名解析)。