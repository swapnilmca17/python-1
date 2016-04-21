-------------

**一个自动发送邮箱验证码的小项目**

-------------

项目说明

*************

1. 使用的邮箱协议是SMTP，使用smtplib库负责邮件发送，使用email.mine.text构造纯文本邮件

2. 验证码code使用的是random模块randint产生的4位伪随机整数

3. emailserver.py文件完成邮件构造和邮件发送功能，使用的邮箱服务器地址是smtp-mail.outlook.com

4. register.py文件完成产生伪随机数和验证功能

使用说明

*************

1. 分别在代码中补充自己的邮箱账号和使用的邮件服务器

2. 在终端用Python命令运行register.py文件即可



