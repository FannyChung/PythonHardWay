# -*- coding: utf-8 -*-
#ex 17 More Files
from sys import argv
from os.path import exists#ʹ��exists������Ὣ�ļ������ַ�����Ϊ�������ж��ļ��Ƿ����

script, from_file, to_file=argv  #��ȡ�����в���

print "Copying from %s to %s"%(from_file,to_file) 

#we could do these two on one line too:
in_file=open(from_file)#���ļ�
indata=in_file.read()#��ȡ�ļ���Ϣ------------------indata = open(from_file).read()Ȼ������ر��ļ�

print "The input file is %d bytes long"%len(indata)#�ļ�����

print "Does the output file exists? %r"%exists(to_file)#�ж�����ļ��Ƿ����
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file=open(to_file,'w')#������ļ�-----------------���û�У����Զ�����
out_file.write(indata)#�Ѵ������ļ���������Ϣд������ļ�

print "Alright, all done."

out_file.close()#�ر�����ļ��������ļ�
in_file.close()

