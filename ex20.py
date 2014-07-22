# -*- coding: utf-8 -*-
#Exercise 20: Functions and Files

from sys import argv

script,input_file=argv

def print_all(f):#打印所有内容
	print f.read()
	
def rewind(f): #使文件指针回到头部
	f.seek(0)  #-------------------seek函数不返回值，设置文件的当前位置偏移，不用再次打开文件
	
def print_a_line(line_count,f):#打印文件的指定行内容
	print line_count,f.readline()
	
current_file=open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a type."

rewind(current_file)#重定位

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+2
print_a_line(current_line,current_file)

current_line=current_line-2
print_a_line(current_line,current_file)
