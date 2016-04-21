#!/usr/bin/python
# -*- coding: UTF-8 -*-

'Mp3player module'

__author__ = 'AJ Kipper'

import os
import mdb
import getpid
Engine = mdb.Engine()

function_dict = {"1":"play","2":"stop","3":"continue","4":"delete","5":"upload"}
class Mp3(object):
	"""docstring for Mp3"""
	def __init__(self):

		pass
	def get_order(self):
		order = raw_input("Click(number): ")
		while order not in function_dict.keys():
			print "Invalid input,please re-enter!"
			order = raw_input("Click(number): ")
		return order

	def interface(self):
		vlaues = Engine.select()
		os.system('clear')
		print "\n"*3+" "*30+"Welcome to Mp3player!\n"
		print " "*32+"List for Songs\n"
		for row in vlaues:
			print " "*25+str(row[0])+":  "+str(row[1])+" —— —— "+str(row[2]) + "\n"
		print " "* 36+"Functions\n"
		print " "* 20+"1.play 2.stop 3.continue 4.delete 5.upload"
		order = self.get_order()
		return function_dict[order]

	def function(self):
	    order = self.interface()
	    if order == "play":
	    	id = raw_input("id:")
	    	vlaues = Engine.select()
	    	for row in vlaues:
	    		if row[0] == int(id):
	    			order = "open " + row[3]
	    			os.popen(order)
	    		else:
	    			continue
	    elif order == "stop":
	    	pid = getpid.getpid()
	    	order = 'kill -STOP ' + pid
	    	os.popen(order)
	    elif order == "continue":
	    	pid = getpid.getpid()
	    	order = 'kill -CONT ' + pid
	    	os.popen(order)
	    elif order == "delete":
	    	Engine.delete()
	    else:
	    	Engine.insert()



if __name__ == '__main__':
	main = Mp3()
	while True:
		main.function()
