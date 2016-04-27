<h4 id = 'CV'>自述</h4>

自己平时用Python写的小项目，各方面都有。

-------------

**目录**

1. [邮件发送 -- smtp-server](#c1)
2. [Mp3播放控制 -- mp3player](#c2)
3. [AppStore数据分析 -- appstore-data-analyse](#c3)
4. [C\S模式聊天室 -- chatting](#c4)
5. [模拟登录人人网 -- simulate-login](#c5)

-------------------

<h5 id = 'c1'>1. 邮件发送 -- smtp-server</h5>

**项目说明**

一个自动发送邮箱验证码的程序

--------------------

1. 使用的邮箱协议是SMTP，使用smtplib库负责邮件发送，使用email.mine.text构造纯文本邮件

2. 验证码code使用的是random模块randint产生的4位伪随机整数

3. emailserver.py文件完成邮件构造和邮件发送功能，使用的邮箱服务器地址是smtp-mail.outlook.com

4. register.py文件完成产生伪随机数和验证功能

直接访问[https://github.com/AJKipper/PythonProject/tree/master/smtp-server](https://github.com/AJKipper/PythonProject/tree/master/smtp-server)

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

具体的项目讲解已经发表在我的博客上，欢迎访问：[AJ Kipper(micronoob.com)](http://cn.micronoob.com/python%E8%BF%9B%E8%A1%8C%E7%AE%80%E5%8D%95%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%EF%BC%8C%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/)

直接访问[https://github.com/AJKipper/PythonProject/tree/master/appstore-data-analyse](https://github.com/AJKipper/PythonProject/tree/master/appstore-data-analyse)

-------------------

<h5 id = 'c4'>4. C\S模式聊天室 -- chatting</h5>

一个基于C/S模式的聊天客户端。

直接访问[https://github.com/AJKipper/PythonProject/tree/master/chatting](https://github.com/AJKipper/PythonProject/tree/master/chatting)

-------------------

<h5 id = 'c5'>5. 模拟登录人人网 -- simulate-login</h5>

模拟浏览器成功登录手机人人网。

直接访问[https://github.com/AJKipper/PythonProject/tree/master/simulate-login](https://github.com/AJKipper/PythonProject/tree/master/simulate-login)
