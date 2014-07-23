# -*- coding: utf-8 -*-
# Exercise 32: Loops and Lists

the_count=[1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for_loop goes throght a list
for number in the_count:
	print "This is count %d"%number
	
#same as above
for fruit in fruits:
	print "A fruit of type: %s"%fruit
	
#also we can go throght mixed lists too notice we have to use %r since we dont't know what's in it
for i in change:
	print"I got %r"%i
	
#we can also build a list
elements=[]

#then use the range function to do 0-5 counts
for i in range(0,6):         #这一循环可以直接用elements=range(0,6)代替
	print "Adding %d to the list."%i
	elements.append(i)
	
for i in elements:
	print "Elements was: %d"%i