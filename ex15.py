#-*- coding: utf-8 -*-
#从sys模块中导入参数变量
from sys import argv
#从argv中解包变量 script,filename
script, filename = argv
#将打开的内容赋值给变量txt
txt = open(filename)
#打印 Here's your file “filename代表的内容”
print "Here's your file %r:" % filename
#打印以txt所赋值为名称的文件的内容
print txt.read()
打印 Type the filename again:
print "Type the filename again:"
#在符号>后输入的值赋给变量file-again
file_again = raw_input(">")
#将打开的内容赋值给变量txt_again
txt_again = open(file_again)
#打印以txt_again所赋值为名称的文件的内容
print txt_again.read()

txt_again.close()