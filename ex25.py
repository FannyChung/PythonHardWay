# -*- coding: utf-8 -*-
# Exercise 25: Even More Practice

def break_words(stuff):
	"""This function will be break up words"""
	words=stuff.split(' ')#用 将所有单词分割开，最后words是一个list
	return words
	
def sort_words(words):
	"""Sort the words"""
	return sorted(words)#将这个list里的所有元素排序
	
def print_first_word(words):#返回第一个元素，同时第一个元素被删除
	"""print the first word after popping it off"""
	word = words.pop(0)
	print word
	
def print_last_word(words):#返回最后一个元素，同时最后一个元素被删除
	"""Print the last word after popping it off"""
	print words.pop(-1)
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words=break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Print the first and last word of the sentence"""
	words=break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sort the words and print the first and last one"""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
