####内置序列类型（ Built-in Sequence Types ）

---

Python中的内置序列类型，普遍具有如下操作方法：

* 成员操作
* 长度测量
* 切片操作
* 迭代操作

下面以```string```类型为代表，做以上的操作：

```
>>> a = 'Python is Great!'
>>> 'P' in a
True
>>> len(a)
16
>>> a[:6]
'Python'
>>> for index in a[:6]:
...     print(index)
...
P
y
t
h
o
n
>>>
```

Python内置序列类型总共有5种，分别是：

1. [字符串（ strings ）](#string)
2. [列表（ lists ）](#list)
3. [元组（ tuples ）](#tuple)
4. [字节数组（ byte arrays ）](#byte_array)
5. [字节（  bytes ）](#byte)

---

<h5 id = 'string'>1. 字符串（ strings ）</h5>

除了数字，字符串也是程序中经常使用的一种类型，大家写的第一个程序```Hello World```就是字符串类型。


