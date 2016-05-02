#!/usr/bin/env python
#-*-coding:utf-8-*-

def Coding(coding_time):
    print 'Programming %d hours per day.' % coding_time
def Relax(relax_time):
    print 'Spending %d hours on sharing my code on Internet.' % relax_time

my_life_time = 10 #live to 100 age，maybe.
for i in range(my_life_time):
    Coding(12)
    Relax(11)
    print 'Spending 1 hours on doing other things.'