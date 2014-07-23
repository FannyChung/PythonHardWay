# -*- coding: utf-8 -*-
# Exercise 34: Accessing Elements of Lists

animals=['bear','python','peacock','kangaroo','whale','platypus']

for i in range(6):
	print "The animal at %d : %s"%(i,animals[i])
	
for i in range(1,7):
	if i ==1:
		str="1rd"
	elif i==2:
		str="2nd"
	elif i==3:
		str="3rd"
	else:
		str="%dth"%i
	print "The %s animal is %s"%(str,animals[i-1])