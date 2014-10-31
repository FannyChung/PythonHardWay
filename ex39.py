# -*- coding: utf-8 -*-
#Exercise 39: Dictionaries, Oh Lovely Dictionaries

#创建州名到缩写的映射
state={"Oregon":'OR',"Florida":"FL","California":"CA","New York":"NY","Michigan":"MI"}

#创建基本的缩写到州名的映射
cities={
    "CA":"San Francisco",#注意一定是：否则会被当成set
	"MI":"Detroit",
	"FL":"Jacksonville"}

#添加一些城市
cities['NY'] = 'New York'
cities['OR']="Portland"

#打印一些城市
print "_"*10
print "NY state has:",cities["NY"]
print"OR state has: ",cities["OR"]

#打印一些州
print"_"*10
print "Michigan's abbreviation is: ",state["Michigan"]
print "Florida's abbreviation is: ",state["Florida"]

#先用state然后cities字典
print"_"*10
print "Michigan has: ",cities[state['Michigan']]
print "Florida has :",cities[state['Michigan']]

#打印每个州的缩写
print"_"*10
for abbre,city in state.items():
	print "%s has the city %s "%(abbre,city)
	
#打印每个州的城市
print"_"*10
for abbre,city in cities.items():
	print"%s has the city %s"%(abbre,city)
	

#同时做
print"_"*10
for stt,abbre in state.items():
	print "%s state is abbreviated %s has city %s"%(stt,abbre,cities[abbre])
	
print"_"*10
#获取一个不存在的州
stt=state.get("Texas")#------------------安全

if not stt:
	print "Sorry, no Texas"
	
#获取一个有默认值的城市
city=cities.get("TX","Does not exist")
print "The city for the state 'TX'  is: %s"%city