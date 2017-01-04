#-*- coding: utf-8 -*-
#从模块sys中导出argv参数
from sys import argv
#将参数解包，并将每个参数赋值给一个变量
script, input_file = argv
#定义函数名（print_all）和变量（f），函数内容为打印f这个文档的内容
def print_all(f):
    print f.read()
#定义函数名（rewind）和变量（f），函数内容为？
def rewind(f):
    f.seek(0)
#定义定义函数名（print_a_line）和变量（line_count, f），函数内容为？
def print_a_line(line_count, f):
    print line_count, f.readline()
#打开文件inpu_file，并定义为变量current_file
current_file = open(input_file)
#打印输出内容“First let's print the whole file:”，空一行
print "First let's print the whole file:\n"
#运行函数print_all
print_all(current_file)
#打印输出内容“Now let's rewind, kind of like a tape.”
print "Now let's rewind, kind of like a tape."
#运行函数rewind
rewind(current_file)
#打印输出内容“Let's print three lines:”
print "Let's print three lines:"
#定义变量current_line并赋值为1；运行函数print_a_line
current_line = 1
print_a_line(current_line, current_file)
#定义变量current_line并赋值为current_line + 1；运行函数print_a_line
current_line = current_line + 1
print_a_line(current_line, current_file)
#定义变量current_line并赋值为current_line + 1；运行函数print_a_line
current_line = current_line + 1
print_a_line(current_line, current_file)