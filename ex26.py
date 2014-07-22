# -*- coding: utf-8 -*-
# Exercise 26: Congratulations, Take a Test!修改程序错误的地方

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):#原来的版本函数定义缺少：  print_first_word(words)
    """Prints the first word after popping it off."""
    word = words.pop(0)#原来的版本拼写错误：  words.poop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)   #原来版本缺少右括号   word = words.pop(-1
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000#原来的版本写错了除号：  jelly_beans \ 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)#原来的版本：拼写start_point错误 ,赋值符号错误： secret_formula(start-point)    == 

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)#原来版本缺少右括号且start_point拼写错误  secret_formula(start_pont


sentence = "All god\tthings come to those who weight."

words = break_words(sentence)#原来的版本：没有import包  ex25.break_words(sentence)
sorted_words = sort_words(words)#原来的版本：没有import包  ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)#原来的版本：多了一个点 .print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)#原来的版本：没有import包  ex25.sort_sentence(sentence)
print sorted_words#原来的版本：拼写print错误  prin sorted_words

print_first_and_last(sentence)#原来的版本：拼写first错误  print_irst_and_last(sentence)

print_first_and_last_sorted(sentence)#原来版本拼写函数和参数、缩进错误   print_first_a_last_sorted(senence)
