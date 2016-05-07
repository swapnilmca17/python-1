#####自述

---
1. 理解上下文

渲染
request
x.html
context ：数据的映射
render(request,x.html,context)


2. 分页器的简单使用

<pre><code>
Python 3.5.0rc1 (v3.5.0rc1:1a58b1227501, Aug  9 2015, 22:13:54) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Django 1.9.6
MozambiqueFreddiefort Vicie Kulas 1 ['Frankie', 'Reynolds', 'II']
UgandaBalistreriberg Lindsey Hills 5 ['Olen', 'Kris', 'DVM']
Timor-LesteNew Newton Dr. Rome Pagac 3 ['Liston', 'Reichel']
AlbaniaNew Orenfort Mrs. Lizeth Johnson 1 ['Hubbard', 'Huels']
>>> from django.core.paginator import Paginator
>>> iter = '1234567890'
>>> paginator = Paginator(iter,4)
>>> paginator.page(1)
<Page 1 of 3>
>>> page1 = paginator.page(1)
>>> page1.object_list
'1234'
>>> page3 = paginator.page(3)
>>> page3.object_list
'90'
>>> page3.has_next()
False
>>> page3.number
3
>>> page3.paginator.num_pages
3
</code>
</pre>