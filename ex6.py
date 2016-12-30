#-*- coding: utf-8 -*-
#定义x变量为There are 10 types of people.
x = "There are %d types of people." % 10
#定义变量binary的值为binary
binary = "binary"
#定义变量do_not为don't
do_not = "don't"
#定义变量y为Those who know binary and those who don't.
y = "Those who know %s and those who %s." % (binary, do_not)
#打印x和y
print x
print y
#打印I said: 'There are 10 types of people.'.
print "I said: %r." % x
#打印I also said: 'Those who know binary and those who don't.'.
print "I also said: '%s'." % y
#定义变量hilarious为false
hilarious = False
#定义变量joke_evaluation为Isn't that joke so funny?! %r
joke_evaluation = "Isn't that joke so funny?! %r" 
#打印Isn't that joke so funny?! False
print joke_evaluation % hilarious
#定义变量w，e为等号后面的内容
w = "This is the left side of..."
e = "a string with a right side."
#打印This is the left side of...a string with a right side.
print w, e