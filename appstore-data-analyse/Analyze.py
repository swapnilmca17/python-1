#!/usr/bin/env Python
#-*- coding: utf-8 -*-
#--Python_Version:2.7.9

'.csv data analyze module'
__version__ = 0.1

__author__ = "AJ Kipper"

from __future__ import division
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import pandas as pd
import sys

frame_data = pd.read_csv('//Users/Jason/Desktop/appstore.csv')
dict_test = dict(frame_data)
def get_values(key):
    '''Output the value of the specified key (get rid of the repeat)'''
    list_val = []
    for item in dict_test[key]:
        if item not in list_val:
            list_val.append(item)
    return list_val
def get_val_nums(key,list_val):
    '''Returns the frequency of the value of the specified key'''
    list_val_num = []
    for val in list_val:
        i = 0
        for item in dict_test[key]:
            if item == val:
                i += 1
        list_val_num.append(i)
    return list_val_num 
list_val = get_values('genre')
list_val_num = get_val_nums('genre',list_val)

#Returns the frequency of the value and the value of the specified key, and converts it to a dict
dict_data = dict(zip(list_val,list_val_num))

for item in dict_data:
    print item,"       频次：",dict_data[item]


'''或者将百分比低于precent_num的value合并为“其他”类别
def regular(list_val,list_val_num,base_num,precent_num):
    sum = 0
    for item in list_val:
        if dict_data[item]/base_num < precent_num:
            sum += dict_data.pop(item)
    list_val = dict_data.keys() + ['其他']
    list_val_num = dict_data.values() + [sum]
    return list_val,list_val_num
list_val,list_val_num = regular(list_val,list_val_num,888,0.05)
dict_data = dict(zip(list_val,list_val_num))
count = 0
for item in dict_data:
    count += 1
    print count,":",item,"       频次：",dict_data[item]
'''

########################################
#              Visual output
########################################

list_val = ['Education','News','Business','Sports','Lifes','Medical','Others']
labels = list_val
sizes = list_val_num
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','m','yellow']
explode = (0, 0.1, 0, 0,0,0,0)
plt.title('Title:AppStore Analysis')
plt.pie(sizes, explode=explode, labels=labels,colors = colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.show()

list_val = ['Education','News','Business','Sports','Lifes','Medical','Others']
labels = list_val
sizes = list_val_num
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','m','yellow']
explode = (0, 0.1, 0, 0,0,0,0)
plt.title('Title:AppStore Analysis')
plt.pie(sizes, explode=explode, labels=labels,colors = colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.show()
