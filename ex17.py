# -*- coding: utf-8 -*-
#ex 17 More Files
from sys import argv
from os.path import exists#使用exists命令，它会将文件名字字符串作为参数，判断文件是否存在

script, from_file, to_file=argv  #获取命令行参数

print "Copying from %s to %s"%(from_file,to_file) 

#we could do these two on one line too:
in_file=open(from_file)#打开文件
indata=in_file.read()#读取文件信息------------------indata = open(from_file).read()然后无需关闭文件

print "The input file is %d bytes long"%len(indata)#文件长度

print "Does the output file exists? %r"%exists(to_file)#判断输出文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file=open(to_file,'w')#打开输出文件-----------------如果没有，会自动创建
out_file.write(indata)#把从输入文件读到的信息写到输出文件

print "Alright, all done."

out_file.close()#关闭输出文件和输入文件
in_file.close()

