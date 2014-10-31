# -*- coding: utf-8 -*-
# 自定义一个字典，命名为hashmap

def new(num_buckets=256):#用空列表初始化字典
	"""initialize a map with the given number of buckets."""
	aMap=[]
	for i in range(num_buckets):
		aMap.append([])
	return aMap
	
def hash_key(aMap,key):#
	"""Given a key this will create a number and then convert it to an index for the aMap's buckets."""
	return hash(key)%len(aMap)
	
def get_bucket(aMap,key):
	"""Given a key, find the bucket where it would go."""
	bucket_id=hash_key(aMap,key)
	return aMap[bucket_id]
	
def get_slot(aMap,key,default=None):
	"""Returns the index,key,and value of a slot found in a bucket."""
	bucket=get_bucket(aMap,key)
	
	for i,kv in enumerate(bucket):
		k,v=kv
		if key==k:
			return i,k,v
		
	return -1,key,default
	
def get(aMap,key,default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i,k,v=get_slot(aMap,key,default=default)
	
def set(aMap,key,value):
	"""Set the key to the value,replacing any existing value"""
	bucket=get_bucket(aMap,key)
	i,k,v=get_slot(aMap,key)
	
	if i>=0:
		#key 存在，替换
		bucket[i]=(key,value)
	else:
		bucket.append((key,value))
		
def delete(aMap,key):
	"""Delete the given key from the map."""
	bucket=get_bucket(aMap,key)
	
	for i in xrange(len(bucket)):
		k,v=bucket[i]
		if key==k:
			del bucket[i]
			break
			
def list(aMap):
	"""Print out what's in map"""
	for bucket in aMap:
		if bucket:
			for k,v in bucket:
				print k,v