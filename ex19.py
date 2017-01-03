#-*- coding: utf-8 -*-
#定义函数，函数名为cheese_and_crackers,括号里为函数的两个参数,函数的作用是打印输出下面的四行内容（其中包含传入的内容）
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#打印下面"We can just give the function numbers directly:"，同时函数传入的内容为数字，运行函数，并打印	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#打印下面"We can just give the function numbers directly:"，同时函数传入的内容为变量，运行函数，并打印	
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#打印下面"We can just give the function numbers directly:"，同时函数传入的内容为数学表达式，运行函数，并打印	
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#打印下面"We can just give the function numbers directly:"，同时函数传入的内容为变量和数学表达式，运行函数，并打印	
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#附加练习
def party(people, money, whole_money):
    print "The party has %d people." % people
    print "Everyone should pay %d for the party." % money
    print "The whole money is %d." % whole_money
    print "Alright.\n"
#第一种
party(10, 30, 10 * 30)
#第二种
people_number = 10
amount_of_money = 30
amount_of_whole_money = people_number * amount_of_money
party(people_number, amount_of_money, amount_of_whole_money)
#第三种

