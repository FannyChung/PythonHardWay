# -*- coding: utf-8 -*-
#ex 18 Names, Variables, Code, Functions

#将函数看作mini 脚本
#通过解包
def print_two(*args):
	arg1,arg2=args#解包
	print "arg1: %r, arg2: %r"%(arg1,arg2)

#接受实参，跳过解包，直接使用变量名
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2:%r"%(arg1,arg2)

def print_one(arg1):
	print "arg1: %r"%arg1
	
def print_none():
	print "I got nothing"
	
print_two("Fanny","Chung")
print_two_again("Fanny","Chung")
print_one("One")
print_none()